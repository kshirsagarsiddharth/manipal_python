# Files Objects 
#%%
with open('test.txt','r') as f:
    # the read of f reads only first 100 lines
    size_to_read = 10
    f_contents = f.read(size_to_read) 
    # this tells us that we are at the 10th position of the 
    # file 
    print(f.tell())
    # this loop reads the contents of the files
    # in the length of 100 
    # if the contents > 0 we print the file 
    # contents and proceed to next 100 chunks 
    # and if the execution exhausts the loop halts 
    #while len(f_contents) > 0:
    #    print(f_contents, end='****')

       # f_contents = f.read(size_to_read)
# %%

with open('test.txt','r') as f:
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    # this statement takes the file pointer to the top of 
    # the file 
    f.seek(0) # use to change position to any point in the file 

    f_contents = f.read(size_to_read)
    print(f_contents)
    #print(f.tell())
# %%

with open('test2.txt','w') as f: 
    # in this case we open the text file 
    # and to this text file we add a Test string 
    # and once we call the seek method the file pointer
    # reaches to the top and overwrites the file and this depends on the pointers 

    f.write('Test')
    f.seek(0)
    f.write('R')

# %%
with open('IMG_20190511_203353.jpg','rb') as rf: 
    with open('text2.jpg','wb') as wf: 
        chunk_size = 4096 
        # readng this much data from the original picture 
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
    
# %%
