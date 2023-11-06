import requests
import json

# curl -H X-CDD-Token:$TOKEN 'https://app.collaborativedrug.com/api/v1/vaults/23/protocols?async=true'
class Session:
    def __init__(self,url,token):
        self.url = url
        self.token = token
        self.headers = {'X-CDD-Token':self.token}
        
    def get(self, endpoint):
        response = requests.get(url=endpoint, headers=self.headers)
        return json.loads(response.text)
    
    def get_compound(self, vault_id):
        '''/vaults/<vault_id>/molecules/<id>'''
        return self.get(self.url+'/vaults/%i/molecules/%s'%(vault_id, str(compound_id)))
    
    def get_all_compounds(self, vault_id, page_size = 1000):
        '''/vaults/<vault_id>/molecules/async=true'''
        return self.get(self.url+'/vaults/%i/molecules/async=true'%(vault_id, str(compound_id)))
    