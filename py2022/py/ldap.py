import ldap3


ad_name='DC=ipap,DC=local'
search_base ='DC=ipap,DC=local'
server_win_uri = '10.1.6.158'
search_filter = "(&(objectClass=person)(sAMAccountName=*)(telephoneNumber=*))"
win_bind_name = "connector@ipap.local"
win_bind_passwd = "123456"
attrs = ['sAMAccountName','telephoneNumber']

def get_users_win_data(ip,search_base,search_filter,attrs,win_bind_name,win_bind_passwd):
    server = ldap3.Server('ldap://{}'.format(ip))
    with ldap3.Connection(server,user=win_bind_name,password=win_bind_passwd) as conn:
        conn.search(search_base, search_filter, attributes=attrs)
        return(conn.entries)
  
  
data2=get_users_win_data(server_win_uri,ad_name,search_filter,attrs,win_bind_name,win_bind_passwd)




# 
for line in data2:
    print('---------------------------------------------------------------------------------')
    #print(line)
    subst1 = (str(line)).split('sAMAccountName: ')
    #print(subst1[1])
    subst2 = subst1[1].split('telephoneNumber: ')
    print(subst2[0])
    print(subst2[1])
     
    
    