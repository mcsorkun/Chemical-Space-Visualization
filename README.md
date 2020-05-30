# Chemical Space Visualization
A simple code for visualization of chemical space of give material dataset. The code requires two columns from datasets (formula and prototype). Prototypes define the structure of materials (like space-groups).


![alt text](https://raw.githubusercontent.com/mcsorkun/Chemical-Space-Visualization/master/images/chemical_space.png)


Dark colors indicate the regions strongly represented in the dataset, while light colors indicate the regions weakly presented. White colors indicate the regions not covered by dataset.

### Dependencies
- matplotlib==3.1.3
- seaborn==0.10.0
- pandas==0.25.1
