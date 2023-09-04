class Categories:
    """Maintain the category list and provide some methods."""
    def __init__(self):
        self._categories = ['expense', ['food', ['meal', 'snack', 'drink'], 'transportation', ['bus', 'railway','MRT']], 'income', ['salary', 'bonus','allowance']]
    
    def view(self):
        """view the categories that was established."""
        def view_categories(categories,level=0):
            if categories == None:
                return
            if type(categories) in {tuple,list}:
                for child in categories:
                    view_categories(child,level + 1)
            else:
                print(f'{"  "*(level-1)}{"-"}{categories}')
        view_categories(self._categories)
    
    def is_category_valid(self,val):
        """Check whether the catecory in the categories that has been established"""
        def check_category_valid(L, val):                                   
            if type(L) in {list, tuple}:
                for i, v in enumerate(L):
                    p = check_category_valid(v, val)
                    if p == True:
                        return (i,)
                    if p != False:
                        return (i,) + p
            return L == val
        return check_category_valid(self._categories,val)

    def find_subcategories(self,category):
        """find the subcategories you want"""
        def find_subcategories_gen(category, categories, found=False):
            if type(categories) == list:
                for index, child in enumerate(categories):
                    yield from find_subcategories_gen(category, child, found)
                    if child == category and index + 1 < len(categories) \
                        and type(categories[index + 1]) == list:
                        # When the target category is found,
                        # recursively call this generator on the subcategories
                        # with the flag set as True.
                        yield from find_subcategories_gen(category, categories[index + 1], True)
            else:
                if categories == category or found == True:
                    yield categories
        return [i for i in find_subcategories_gen(category,self._categories)]

