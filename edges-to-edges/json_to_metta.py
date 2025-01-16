from json import loads

untyped = True


def dict_generator(indict, pre=None):
    pre = pre[:] if pre else []
    if isinstance(indict, dict):
        if untyped and "@value" in indict and "@type" in indict:
            yield pre + [indict["@value"]]
            return
        for key, value in indict.items():
            if isinstance(value, dict):
                yield from dict_generator(value, pre + [key])
            elif isinstance(value, list) or isinstance(value, tuple):
                # TODO support arbitrary depth lists
                for i, v in enumerate(value):
                    if isinstance(v, list) or isinstance(v, tuple):
                        for j, v_ in enumerate(v):
                            if isinstance(v_, list) or isinstance(v_, tuple):
                                for k, v__ in enumerate(v_):
                                    yield from dict_generator(v__, pre + [(key, i, j, k)])
                            else:
                                yield from dict_generator(v_, pre + [(key, i, j)])
                    else:
                        yield from dict_generator(v, pre + [(key, i)])
            else:
                yield pre + [key, value]
    else:
        yield pre + [indict]


with open("InteractiveDisneyStrategy.json") as f:
    ds = [loads(line) for line in f.readlines()]

import os

def convert(json_file, metta_file):
    try:
        with open(json_file) as f:
            data = f.read()
            # Conversion logic here
            with open(metta_file, 'w') as mf:
                mf.write(data)  # Placeholder for actual conversion logic
    except FileNotFoundError:
        print(f"Error: The file '{json_file}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    json_file = "InteractiveDisneyStrategy.json"
    metta_file = "InteractiveDisneyStrategy.metta"
    convert(json_file, metta_file)

with open("InteractiveDisneyStrategy.metta", "w") as f:
    for i, d in enumerate(ds):
        for path in dict_generator(d):
            s = path[-1]
            # TODO escape strings
            if isinstance(s, str):
                s = '"' + s + '"'

            for item in reversed(path[:-1]):
                if isinstance(item, tuple):
                    s = f"({' '.join(map(str, item))} {s})"
                else:
                    s = f"({item} {s})"
            if len(ds) == 1:
                f.write(s + "\n")
            else:
                f.write(f"(json {i} {s})\n")
