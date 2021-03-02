#%%
try:
    f = open('test.txt')
    if f.name == 'test.txt':
        print('u')
        raise Exception
    #var = bad_var
except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(e.__class__)



# %%
