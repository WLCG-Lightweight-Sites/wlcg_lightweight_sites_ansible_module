import argparse, yaml

def augment(site_level_configuration_file, config_schema):
    input_config_file = yaml.load(site_level_configuration_file)
    schema = yaml.load(config_schema)

    for (each in schema['available-from-site-level-config']):
        input_config_file[each] = schema[each]

    f = open('complete_config.yaml', 'w'):
    f.write(yaml.dump(input_config_file)) 

if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument('filename', type=argparse.FileType('r'))
    parser.add_argument('filename2', type=argparse.FileType('r'))
    args = parser.parse_args()
    output = augment(args.filename, args.filename2)