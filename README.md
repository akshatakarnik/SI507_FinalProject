# SI507_FinalProject_PhylogeneticTree

This is the program I made for the intermediate programming class I took at U Mich. The program provides information about a species of interest to the user. It displays a basic phylogenetic tree, species scientific classification, habitat and threats.

## Data Sources

I utilised the IUCN APIs to access information about a species scientific classification, threats, and habitats. All the data was in JSON format

•	https://apiv3.iucnredlist.org/api/v3/docs#threat-name

•	https://apiv3.iucnredlist.org/api/v3/docs#habitat-name

•	https://apiv3.iucnredlist.org/api/v3/docs#species-individual-name

## Data Structure

I used a binary tree structure to present the data. The user was given an option between two classes to select from. Once the user selected a class, they were presented two orders to select from and finally two families within this order. Once the user selected a family, they were given a list of the species in this family from which they can pick a species to know more about.

## How it works

1) The program has a built in list for species belonging to each family the user can select. Once the user picks a family, the program displays the list of species and prompts the user to pick one.
2) After the user selects the species, the program scrapes the relevant information from the above IUCN API. This is then presented in the form of text and a phylogenetic tree.

## Running the program

1) Download the code file. 
2) Install packages requests, and treelib.
3) Run the program in prefered python interpreter.
