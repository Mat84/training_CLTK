#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install cltk


# In[2]:


from cltk.corpus.utils.importer import CorpusImporter


# In[3]:


my_greek_downloader = CorpusImporter('greek')


# In[4]:


my_greek_downloader.list_corpora


# In[5]:


my_greek_downloader.import_corpus('tlg', 'C:\Program Files (x86)\TLG\TLG-E')


# In[6]:


my_greek_downloader.import_corpus('phi7', 'C:\Program Files (x86)\TLG\PHI-7')


# In[7]:


my_greek_downloader.import_corpus('greek_software_tlgu')


# In[8]:


my_greek_downloader.import_corpus('greek_text_perseus')


# In[9]:


my_greek_downloader.import_corpus('greek_proper_names_cltk')


# In[10]:


my_greek_downloader.import_corpus('greek_models_cltk')


# In[11]:


my_greek_downloader.import_corpus('greek_treebank_perseus')


# In[14]:


my_greek_downloader.import_corpus('greek_lexica_perseus')
my_greek_downloader.import_corpus('greek_training_set_sentence_cltk')


# In[17]:


my_greek_downloader.import_corpus('greek_word2vec_cltk')


# In[20]:


my_greek_downloader.import_corpus('greek_text_tesserae')


# In[21]:


my_greek_downloader.import_corpus('greek_text_first1kgreek')


# In[28]:


ls -l C:\Users\Matteo\cltk_data\greek\text\greek_text_first1kgreek


# In[25]:


from cltk.corpus.greek.tei import onekgreek_tei_xml_to_text


# In[30]:


pip install bs4 


# In[32]:


from bs4 import BeautifulSoup


# In[33]:


onekgreek_tei_xml_to_text()


# In[34]:


tlg.list_corpora


# In[35]:


my_greek_downloader.import_corpus('tlg', 'C:\Program Files (x86)\TLG\TLG-E')


# In[ ]:





# In[40]:


from cltk.corpus.greek.tlgu import TLGU


# In[42]:


ls C:\Users\Matteo\cltk_data\greek\software\greek_software_tlgu


# In[50]:


from cltk.corpus.utils.importer import CorpusImporter




# In[51]:


my_latin_downloader = CorpusImporter('latin')


# In[52]:


my_latin_downloader.list_corpora


# In[53]:


my_latin_downloader.import_corpus('phi5', 'C:\Program Files (x86)\TLG\PHI-5')


# In[54]:


my_latin_downloader.import_corpus('phi7', 'C:\Program Files (x86)\TLG\PHI-7')


# In[55]:


from cltk.corpus.utils.importer import CorpusImporter


# In[56]:


t = TLGU()


# In[ ]:




