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
    
    def get_projects(self, vault):
        return self.get(self.url+'/vaults/%s/projects'%str(vault))
    
    def get_compound(self, vault_id, compound_id):
        '''/vaults/<vault_id>/molecules/<id>'''
        return self.get(self.url+'/vaults/%i/molecules/%s'%(vault_id, str(compound_id)))
    
    def check_export(self, vault_id, queue):
        '''vaults/23/export_progress/18765'''
        return self.get(self.url+'/vaults/%i/export_progress/%i'%(vault_id, queue['id']))
    
    # work in progress
    def get_all_compounds(self, vault_id, page_size = 1000, check_sleep_time = 600):
        '''/vaults/<vault_id>/molecules/async=true'''
        # this will queue up the export 
        queue = self.get(self.url+'/vaults/%i/molecules?async=true&page_size=%i'%(vault_id, page_size))
        # this will check status default every 10 minutes
        while self.check_export(vault_id, queue['id'])['status'] in ['new','started']:
            time.sleep(check_sleep_time)
        # when it passes move to download in chunks
        print('DONE!')