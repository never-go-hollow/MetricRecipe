# MetricRecipe

Simple script to convert recipes from imperial to metric system.

## Usage

Sample recipe.txt:
```shell
2/3 pound beef
2 teaspoons Worcestershire sauce
3 ounces mayonaise
1 oz. ketchup
3/4 teaspoon vinegar
4 teaspoons cream
4 tsp. cream
1/4 tablespoons melted butter
3 cups all purpose flour
7 tablespoons butter
1/4 tbsp. salt
1 oz. whipped cream

```

```
$ py converter.py recipe.txt

--------
Servings?
--------
> 2
--------
[0.6 kg] beef
[19.6 ml] Worcestershire sauce
[170.0 g] mayonaise
[56.7 g] ketchup
[7.4 ml] vinegar
[39.2 ml] cream
[39.2 ml] cream
[7.1g] melted butter
[817.8g] all purpose flour
[199.6g] butter
[8.8g] salt
[28.3g] whipped cream  
```