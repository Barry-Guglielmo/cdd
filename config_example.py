
# Global configurations
# You need to have the customer Whitelist the instance IP address
prod_url = "https://app.collaborativedrug.com/api/v1"
test_url = ""

"""
The configuration file uses dictionaries and should be clean to use.
"""
# api key found at "~seurat/.cdd/credentials"
CDD_API_CONFIG = {
                  'url' : prod_url,
                  'api_token' : '',
                  'vaults':'0000', # vault
                  'async':'true',
                  'page_size':1000, # 1000 is max
                  }

SIMPLE_SCHEMA_DB_CONFIG = {
                           "database":"cdd", 
                           "user":'postgres', 
                           "password":'postgres', 
                           "host":'127.0.0.1', 
                           "port": '5432' # on production 3247 on local probably 5432
                           }

# with k8s this will be set to cloud sql or persistant volume
IMAGE_SERVICE_DB_CONFIG = {
                            'path':'plots.db'
                          }

# NOTE: Change in names on LD side will break this! Only specified Projects will be brought over
# No automated system for creating LD projects. Please create project manually.
# Need to write this so there can be a list of LD projects as well

# For Now Projects are 1:1
# we rely on them to have data in multiple projects in CDD
CDD_PROJECTS_CONFIG = {   # CDD Project PK : LD Proj Name
                                6784367: 'CCNE',
                                6744140: 'CDK2',
                                6752506: 'MEN1',
                                6784366: 'PIK3CA',
                                6777306: 'PIK3CD',
                                6777305: 'PKMYT1',
                                6744929: 'Cov Lys Lib',
                                6743812: 'Library NC',
                                # 827071: 'NONE',
                                6777304: 'LifeChem Cys Cov Lib',
                                6818265: 'A&CSP1',
                                6818266: 'EPP Set',
                                6827765: 'MiscProbes',
                                6744066: 'Library Cov',
                                7080986: 'AKT E17K'
                    }


PIVOT_CONDITIONS = {
                    # 'NAME OF STUDY OR TYPE?': [' PIVOT FIELD 1',...]
                    'TR-FRET': ['protein'],
                    'AlphaLISA':['cellline']
                    }

# will be used in pivot name
PIVOT_DELIMITER = " "

# Alias assay or pivoted assays
ASSAY_ALIAS = {}