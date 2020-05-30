inventory = {'메로나':[300, 20], '비비빅':[400,3], '죠스바':[250,100]}
print(inventory)

m_p = inventory.get('메로나')[0]
print(m_p)

m_n = inventory.get('메로나')[1]
print(m_n)

inventory['월드콘'] = [500, 7]
print(inventory)