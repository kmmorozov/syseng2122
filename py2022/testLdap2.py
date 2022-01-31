from ldap3 import Server, Connection, SASL, DIGEST_MD5,SUBTREE
##import ldap3 as ldap
##from ldap3 import Connection, Server, SIMPLE, SYNC, SUBTREE, ALL

server = Server(host = '192.168.20.21', port = 389)
conn = Connection(server, auto_bind = True, version = 3, client_strategy = 'SYNC', authentication = SASL,
                         sasl_mechanism = DIGEST_MD5, sasl_credentials = (None, 'administrator', '123qaz!', None))
print('test')
print(conn.bind())
print('test2')
# 
# user_dn = "cn=administrator,ou=users,ou=data,ou=prod,ou=authserver,dc=asterisk,dc=AAA"
# base_dn = "dc=asterisk,dc=AAA"
# filter = "uid=admin"
# total_entries = 0
# conn.search(search_base = 'dc=asterisk,dc=AAA',
#          ##search_filter = '(objectClass=inetOrgPerson)',
#          search_filter = '(objectCategory=Person)',            
#          search_scope = SUBTREE,
#          attributes = ['cn', 'givenName'],
#          paged_size = 5)
# total_entries += len(conn.response)
# #result = conn.search(search_base=base_dn, search_filter=filter, search_scope=SUBTREE)
# #logger.info('SEARCHING COMPLETE') #does not appear in the log
# # return all user data results
# for entry in conn.response:
#     print(entry)
#     ##print(entry['dn'], entry['attributes'])
# conn.unbind()