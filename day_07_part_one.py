import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_07.data")

with open(filename) as f:
    print('reading file...')
    lines = map(lambda x: (x.strip()), f.readlines())
    bag_rules = list(map(lambda x: (tuple(x.split('contain'))), lines))

    def contains(bag):
        containing_bags = []
        for rule in bag_rules:
            if bag in rule[1]:
                containing_bag = rule[0].replace("'","").strip()
                containing_bags.append(containing_bag[:-5])
        return containing_bags


    containing_bags = list(dict.fromkeys(contains('shiny gold')))

    while True:
        all_new_bags = []
        for bag in containing_bags:
            new_bags = contains(bag)
            for new_bag in new_bags:
                if new_bag not in containing_bags:
                    all_new_bags.append(new_bag)
        all_new_bags = list(dict.fromkeys(all_new_bags))
        if len(all_new_bags) == 0:
            break
        for new_bag in all_new_bags:
            containing_bags.append(new_bag)

    print(len(containing_bags))