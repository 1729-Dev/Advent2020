import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "day_07.data")

with open(filename) as f:
    lines = map(lambda x: (x.strip()), f.readlines())
    bag_rules = list(map(lambda x: (tuple(x.split('contain'))), lines))

    def holds_what_bags(bag):
        # shiny gold ==> 2 dark red
        held_bags = []
        for bag_rule in bag_rules:
            if bag in bag_rule[0]:
                if 'no other bags.' in bag_rule[1]:
                    return []
                rule_list = bag_rule[1].split(',')
                for rule in rule_list:
                    held_bags.append(rule.replace("'","").replace(".","").replace("bags","").replace("bag","").strip())
        return held_bags

    def holds_bags(bag):
        for bag_rule in bag_rules:
            if bag in bag_rule[0] and 'no other bags' in bag_rule[1]:
                return False
        return True

    def replace_bags(description):
        # 2 dark red bags ==> [dark orange, dark orange]
        replacement = []
        containing_quantity = int(description[:1])
        bags_this_holds = holds_what_bags(description[2:])
        for holds in bags_this_holds:
            for _ in range(containing_quantity):
                bag_quantity = int(holds.strip()[:1])
                for _ in range(bag_quantity):
                    replacement.append(holds.strip()[2:])
        return replacement

    top_bags = holds_what_bags('shiny gold')

    total_bag_count = 0
    while len(top_bags) > 0:
        for bag in top_bags:            
            bag_colour = bag[2:]
            bag_quantity = int(bag[:1])
            if holds_bags(bag_colour):
                new_bags = replace_bags(bag)
                top_bags.remove(bag)
                total_bag_count += bag_quantity
                for new_bag in new_bags:
                    top_bags.append(f"1 {new_bag}")
                continue
            if not holds_bags(bag_colour):
                top_bags.remove(bag)
                bag_quantity = int(bag[:1])
                total_bag_count += bag_quantity
                continue
            raise Exception('what???')

    print(total_bag_count)
