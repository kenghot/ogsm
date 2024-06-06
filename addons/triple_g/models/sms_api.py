# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models
from odoo.addons.iap.tools import iap_tools
import requests
from xml.etree.ElementTree import fromstring, ElementTree
DEFAULT_ENDPOINT = 'https://iap-sms.odoo.com'


class SmsApi(models.AbstractModel):
    _inherit = 'sms.api'


    @api.model
    def _contact_iap(self, local_endpoint, params):
        try:
            # account = self.env['iap.account'].get('sms')
            # params['account_token'] = account.account_token
            # endpoint = self.env['ir.config_parameter'].sudo().get_param('sms.endpoint', DEFAULT_ENDPOINT)
            # # TODO PRO, the default timeout is 15, do we have to increase it ?

            # return iap_tools.iap_jsonrpc(endpoint + local_endpoint, params=params)

            #kenghot
            # params = {message: [{'res_id': 13, 'number': '66924696655', 'content': 'Dear Deco Addict, it seems that some of your payments stay unpaid'}]}
            #api = [{'state': 'unregistered', 'res_id': 13, 'request_id': 'error', 'credit': 0}]
            url = self.env['ir.config_parameter'].sudo().get_param('sms.configuration', DEFAULT_ENDPOINT)
            # TODO PRO, the default timeout is 15, do we have to increase it ?
            #http://www.thaismartsms.com/api/api.php?username=mgsolution&password=12345678&sender=DEPFUND&msisdn=%s&message=%s
            resp = []
            for sms in params['messages']:
                msg = url % (sms['number'], sms['content'])
                response = requests.get(msg)
                response.raise_for_status()
                #resp = response.json()
                if response.status_code  == 200:
                    tree = ElementTree(fromstring(response.text))
                    root = tree.getroot()
                    details = root.findall("Detail")
                    if len(details) > 0:
                        resp.append({'state':'server_error','res_id':sms['res_id'],'request_id': 'error','credit':0})
                    else:
                        resp.append({'state':'sent','res_id':sms['res_id'],'request_id': 'sent','credit':1})
                else:
                    resp.append({'state':'server_error','res_id':sms['res_id'],'request_id': str(response.status_code) ,'credit':0})
            return resp
    #        return [{'state': 'unregistered', 'res_id': params[0]['res_id'], 'request_id': 'error', 'credit': 0}]
        except Exception as e:
            return [{'state': 'server_error', 'res_id': params[0]['res_id'], 'request_id': e, 'credit': 0}]
    @api.model
    def _send_sms(self, numbers, message):
        """ Send a single message to several numbers

        :param numbers: list of E164 formatted phone numbers
        :param message: content to send

        :raises ? TDE FIXME
        """
        params = {
            'numbers': numbers,
            'message': message,
        }
        return self._contact_iap('/iap/message_send', params)

    @api.model
    def _send_sms_batch(self, messages):
        """ Send SMS using IAP in batch mode

        :param messages: list of SMS to send, structured as dict [{
            'res_id':  integer: ID of sms.sms,
            'number':  string: E164 formatted phone number,
            'content': string: content to send
        }]

        :return: return of /iap/sms/1/send controller which is a list of dict [{
            'res_id': integer: ID of sms.sms,
            'state':  string: 'insufficient_credit' or 'wrong_number_format' or 'success',
            'credit': integer: number of credits spent to send this SMS,
        }]

        :raises: normally none
        """
        params = {
            'messages': messages
        }
        return self._contact_iap('/iap/sms/2/send', params)
