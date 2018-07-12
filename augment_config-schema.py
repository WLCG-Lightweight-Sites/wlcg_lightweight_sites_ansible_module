import sys, yaml

if __name__ == "__main__":
    augcc = open('augmented_complete_config.yaml', 'r+')
    yaugcc = yaml.load(augcc.read())

    new = {str(sys.argv[2]): str(sys.argv[3])}
    yaugcc['lightweight_components'][int(sys.argv[1])]['config'][0]['cream-info'].update(new)
    augcc.close()

    modify_augcc = open('augmented_complete_config.yaml', 'w')
    modify_augcc.write(yaml.dump(yaugcc))
    modify_augcc.close()