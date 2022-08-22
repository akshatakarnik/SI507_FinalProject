#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import requests
from treelib import Node, Tree


# In[2]:


#Making list of species in famil, making 8 lists for each family
#m_c_f <- mammals_carnivora_felidae, m_c_c <- mammals_carnivora_canidae, m_a_c <- mammals_artiodactyla_cervidae
#m_a_b <- mammals_artiodactyla_bovidae
#a_c_c <- aves_charadriiformes_charadriidae, a_c_s <- aves_charadriiformes_scolopacidae, 
#a_co_a <- aves_coraciiformes_alcedinidae, a_co_m <- aves_coraciiformes_meropidae
m_c_c = ["Canis aureus (Golden jackal)", "\nCanis lupus pallipes (Indian wolf)", "\nCuon alpinus (Dhole)",         "\nVulpes bengalensis (Bengal fox)", "\nVulpes ferrilata (Tibetan fox)", "\nVulpes vulpes (Red fox)"]
m_c_f = ["Acinonyx jubatus venaticus (Asiatic cheetah)","\nCaracal caracal (Caracal)", "\nCatopuma temminckii (Asian golden cat)",         "\nFelis chaus (Jungle cat)", "\nFelis lybica ornata (Asiatic wildcat)", "\nLynx lynx (Eurasian lynx)",         "\nNeofelis nebulosa (Clouded leopard)", "\nOtocolobus manul (Pallas's cat)", "\nPanthera tigris tigris (Bengal tiger)",         "\nPanthera leo (Lion)", "\nPanthera pardus (Indian leopard)", "\nPanthera uncia (Snow leopard)", "\nPardofelis marmorata (Marbled cat)",         "\nPrionailurus bengalensis (Leopard cat)", "\nPrionailurus rubiginosus (Rusty-spotted cat)", "\nPrionailurus viverrina (Fishing cat)"]
m_a_c = ["Axis axis (Chital)", "\nAxis porcinus (Indian hog deer)", "\nCervus hanglu (Central Asian red deer)",         "\nCervus elaphus (Kashmir stag)", "\nMuntiacus muntjak (Indian muntjac)", "\nMuntiacus putaoensis (Leaf muntjac)",          "\nRucervus duvaucelii (Barasingha)", "\nRucervus eldii (Eld's deer)", "\nRusa unicolor (Sambar deer)"]
m_a_b = ["Antilope cervicapra (Blackbuck)", "\nBos gaurus (Gaur)", "\nBos javanicus (Banteng)", "\nBos mutus (Wild yak)",         "\nBos primigenius namadicus (Indian aurochs)", "\nBubalus arnee (Wild water buffalo)", "\nCapra falconeri (Markhor)",         "\nGazella bennettii (Chinkara)", "\nPseudois nayaur (Bharal)", "\nHemitragus jemlahicus (Himalayan tahr)",         "\nTetracerus quadricornis (Four-horned antelope)", "\nCapra sibirica (Siberian ibex)"]
a_c_c = ["Vanellus vanellus (Northern lapwing)", "\nVanellus duvaucelii (River lapwing)", "\nVanellus malabaricus (Yellow-wattled lapwing)",         "\nVanellus indicus (Red-wattled lapwing)", "\nCharadrius hiaticula (Common ringed plover)",         "\nCharadrius dubius (Little ringed plover)", "\nCharadrius alexandrinus (Kentish plover)",         "\nCharadrius mongolus (Lesser sand plover)", "\nCharadrius leschenaultii (Greater sand plover)",         "\nPluvialis squatarola (Grey plover)"]
a_c_s = ["Numenius phaeopus (Eurasian whimbrel)", "\nNumenius arquata (Eurasiam curlew)", "\nLimosa lapponica (Bar-tailed godwit)",         "\nLimosa limosa (Black-tailed godwit)", "\nArenaria interpres (Ruddy turnstone)", "\nCalidris tenuirostris (Great knot)",         "\nCalidris canutus (Red knot)", "\nCalidris ferruginea (Curlew sandpiper)", "\nCalidris pygmaea (Spoon-billed sandpiper)",         "\nCalidris minuta (Little stint)", "\nTringa nebularia (Common greenshank)", "\nTringa totanus (Common redshank)"]
a_co_a = ["Pelargopsis capensis (Stork-billed kingfisher)", "\nPelargopsis amauroptera (Brown-winged kingfisher)", "\nHalcyon coromanda (Ruddy kingfisher)",         "\nHalcyon smyrnensis (White-throated kingfisher)", "\nHalcyon pileata (Black-capped kingfisher)",         "\nTodiramphus chloris (Collared kingfisher)", "\nAlcedo meninting (Blue-eared kingfisher)", "\nAlcedo atthis (Common kingfisher)",         "\nCeyx erithaca (Oriental dwarf kingfisher)", "\nMegaceryle lugubris (Crested kingfisher)", "\nCeryle rudis (Pied kingfisher)"]
a_co_m = ["Nyctyornis athertoni (Blue-bearded bee-eater)", "\nMerops orientalis (Asian green bee-eater)", "\nMerops persicus (Blue-cheeked bee-eater)",         "\nMerops philippinus (Blue-tailed bee-eater)", "\nMerops viridis (Blue-throated bee-eater)", "\nMerops leschenaulti (Chestnut-headed bee-eater)",         "\nMerops apiaster (European bee-eater)"] 


# In[5]:


def main():
    """This function executes the program. It prompts the user to answer a series of questions and finally displays
    information for the species the user selects"""
    print("Welcome! This program helps you to find information about a species scientific classification, it's habitat and the threats to the species. It also displays a phylogenetic tree for the species of interest")
    user_promt()
    user_decision = input("Would you like to know more about another species? (Enter \"yes\" or \"no\"): ")
    while user_decision.lower() != "no":
        user_promt()
        user_decision = input("Would you like to know more about another species? (Enter \"yes\" or \"no\"): ")
        if user_decision.lower() == "no":
            break
    print("Thank you!")
    
class Species_Tree():
    """This class recovers the family tree of the spcies of interest"""
    def __init__(self, kindgom = "kingdom", phylum = "phylum", class_ = "class", order = "order",
                family = "family", genus = "genus", scientific_name = "scientific name", json = "json" ):
        try:
            self.kingdom = json['kingdom']
        except:
            self.kingdom = "No information available"
        try:
            self.phylum = json['phylum']
        except:
            self.phylum = "No information available"
        try:
            self.class_ = json['class']
        except:
            self.class_ = "No information available"
        try:
            self.order = json['order']
        except:
            self.order = "No information available"
        try:
            self.family = json['family']
        except:
            self.family = "No information available"
        try:
            self.genus = json['genus']
        except:
            self.genus = "No information available"
        try:
            self.scientific_name = json['scientific_name']
        except:
            self.scientific_name = "No information available"
        
    def s_tree(self):
        return "Kingdom: " + self.kingdom + "\nPhylum: " + self.phylum + "\nClass: " + self.class_                + "\nOrder: " + self.order + "\nFamily: " + self.family + "\nGenus: " + self.genus                + "\nScientific Name: " + self.scientific_name
        
class Species_Threat():
    """This class parses through the json to get information on threats to species"""
    def __init__(self, threat = "Threat", json = "json"):
        try:
            self.threat = json['title']
        except:
            self.threat = "No information available"
            
    def species_threat(self):
        return self.threat
    
class Species_Habitat():
    """This class parses through the json to get information on the habitat of the species"""
    def __init__(self, habitat = "Habitat", json = "json"):
        try:
            self.habitat = json['habitat']
        except:
            self.habitat = "No information available"
            
    def species_habitat(self):
        return self.habitat
    
def species_tree(sname):
    #print(species_name)
    iucn_species_name_url = "https://apiv3.iucnredlist.org/api/v3/species"
    name = sname 
    token = "94d39ec66b239e9857b15c894d49455943a63719fc1ccc950034cd48d57be3cf"
    name_resp = requests.get(f"{iucn_species_name_url}/{name}?token={token}")
    name_result = json.loads(name_resp.text)['result']
    return name_result

def species_habitat(sname):
    iucn_species_habitat = "https://apiv3.iucnredlist.org/api/v3/habitats/species/name"
    name = sname
    token = "94d39ec66b239e9857b15c894d49455943a63719fc1ccc950034cd48d57be3cf"
    habitat_resp = requests.get(f"{iucn_species_habitat}/{name}?token={token}")
    habitat_result = json.loads(habitat_resp.text)['result']#See which section of this you need
    return habitat_result

def species_threat(sname):
    iucn_species_threat = "https://apiv3.iucnredlist.org/api/v3/threats/species/name"
    name = sname
    token = "94d39ec66b239e9857b15c894d49455943a63719fc1ccc950034cd48d57be3cf"
    threat_resp = requests.get(f"{iucn_species_threat}/{name}?token={token}")
    threat_result = json.loads(threat_resp.text)['result']#See which section of this you need
    return threat_result

def species_tree_result(species_name):
    tree_result = species_tree(species_name)
    tree_list =[]
    for tree in tree_result:
        tree_list.append(Species_Tree(json=tree))
    for b in tree_list:
        print(b.s_tree())
        
def species_habitat_result(species_name):
    habitat_result = species_habitat(species_name)
    habitat_list = []
    for habitat in habitat_result:
        habitat_list.append(Species_Habitat(json=habitat))
    for i in habitat_list:
        print(i.species_habitat())
        
def species_threat_result(species_name):
    t_result = species_threat(species_name)
    threat_list =[]
    for threat in t_result:
        threat_list.append(Species_Threat(json=threat))
    a=1
    for b in threat_list:
        print(a, b.species_threat())
        a+=1
        
def species_information(species_name):
    print("\nSCIENTIFIC CLASSIFICATION")
    tree = species_tree_result(species_name)
    print("\nSPECIES HABITAT")
    habit = species_habitat_result(species_name)
    print("\nTHREATS TO SPECIES")
    threat = species_threat_result(species_name)
    
def view_tree(class_name, order1, order2, fam1, fam2, species):
    class_name_p = class_name.lower()
    order1_p = order1.lower()
    order2_p = order2.lower()
    fam1_p = fam1.lower()
    fam2_p = fam2.lower()
    species_p = species.lower() 
    
    tree = Tree()
    tree.create_node("\nChordata", "chordata")
    tree.create_node("Mammals", "mammals", parent = "chordata")
    tree.create_node("Aves", "aves", parent = "chordata")
    tree.create_node(order1, order1_p, parent = class_name_p)
    tree.create_node(order2, order2_p, parent = class_name_p)
    tree.create_node(fam1, fam1_p, parent = order1_p)
    tree.create_node(fam2, fam2_p, parent = order1_p)
    tree.create_node(species, species_p, parent = fam1_p)
    print("\nPHYLOGENETIC TREE")
    tree.show()
    
def user_promt():
    class_answer = input("Would you like to know more about mammals or aves?: ")
    if class_answer.lower() == "mammals":
        order_answer = input("Would you like to know more about carinovres or artiodactyla?: ")
        if order_answer.lower() == "carnivores":
            family_answer = input("Would you like to know more about felidae or canidae?: ")
            if family_answer == "felidae":
                print(*m_c_f, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name)")
                view_tree("Mammals", "Carnivores", "Artiodactyla", "Felidae", "Canidae", species_name)
                species_information(species_name)
            elif family_answer == "canidae":
                print(*m_c_c, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name)")
                view_tree("Mammals", "Carnivores", "Artiodactyla", "Canidae", "Felidae", species_name)
                species_information(species_name)
        elif order_answer.lower() == "artiodactyla" :
            family_answer = input("Would you like to know more about cervidae or bovidae?: ")
            if family_answer == "cervidae":
                print(*m_a_c, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name)")
                view_tree("Mammals", "Artiodactyla", "Carnivores", "Cervidae", "Bovidae", species_name)
                species_information(species_name)
            elif family_answer == "bovidae": 
                print(*m_a_b, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name) ")
                view_tree("Mammals", "Artiodactyla", "Carnivores", "Bovidae", "Cervidae", species_name)
                species_information(species_name)
    elif class_answer.lower() == "aves":
        order_answer = input("Would you like to know more about charadriiformes or coraciiformes?: ")
        if order_answer.lower() == "charadriiformes":
            family_answer = input("Would you like to know more about charadriidae or scolopacidae?: ")
            if family_answer == "charadriidae":
                print(*a_c_c, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name) ")
                view_tree("Aves", "Charadriiformes", "Coraciiformes", "Charadriidae", "Scolopacidae", species_name)
                species_information(species_name)
            elif family_answer == "scolopacidae" : 
                print(*a_c_s, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name) ")
                view_tree("Aves", "Charadriiformes", "Coraciiformes", "Scolopacidae", "Charadriidae", species_name)
                species_information(species_name)
        elif order_answer.lower() == "coraciiformes":
            family_answer = input("Would you like to know more about alcedinidae or meropidae?: ")
            if family_answer == "alcedinidae":
                print(*a_co_a, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name) ")
                view_tree("Aves", "Coraciiformes", "Charadriiformes", "Alcedinidae", "Meropidae", species_name)
                species_information(species_name)
            elif family_answer == "meropidae" :
                print(*a_co_m, sep="\n")
                species_name = input("Pick a species from the above list about whom you would like to know about? \n(Please enter the scientifc name) ")
                view_tree("Aves", "Coraciiformes", "Charadriiformes", "Meropidae", "Alcedinidae", species_name)
                species_information(species_name)
                

if __name__ == '__main__':
    main()

