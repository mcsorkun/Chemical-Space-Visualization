# -*- coding: utf-8 -*-
"""
Created on Thu Apr 9 15:57:07 2020

@author: Murat Cihan Sorkun
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re


def main():
    # Import data
    df_materials=pd.read_csv('data/materials.csv')  
    

    # Creates list of elements and prototypes in the dataset   
    element_list=[]
    prototype_list=[]
        
    for index, row in df_materials.iterrows():
        elements=create_elemen_list([row["formulas"]])
        for elem in elements:
            element_list.append(elem)
            prototype_list.append(row["prototypes"])
            
    df_elem_proto = pd.DataFrame(element_list, columns=['element'])
    df_elem_proto["prototypes"]=prototype_list
                    
    # Groups counts based of elements and prototypes
    elem_proto_counts = df_elem_proto.groupby(['element', 'prototypes']).size()
    
    # Plots heatmap of chemical space   
    plt.figure(figsize=(18,8))
    aa=elem_proto_counts.unstack(level=0)
    sns.heatmap(aa, cmap="copper_r", linewidths=1, linecolor='black')
    plt.xlabel("Elements", fontweight='bold')
    plt.ylabel("Prototypes", fontweight='bold')


# Creates list of elements covering all elements in the materials
def create_elemen_list(formula_list):
    all_elements_list = []
    for formula in formula_list:
        element_list = re.findall('[A-Z][^A-Z]*', formula)
        for elem in element_list:
            element, number = split_number(elem)
            if element not in all_elements_list:
                all_elements_list.append(element)

    return all_elements_list



# Parses elements and number of occurences from element-number couple
def split_number(text):

    element = text.rstrip('0123456789')
    number = text[len(element):]
    if number == "":
        number = 1
    return element, int(number)



if __name__== "__main__":
    main()




























