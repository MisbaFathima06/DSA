strings=['club','clove','clean','clap']
strings.sort()
print(strings)

def common_prefix(strings):
    result=""

    first=strings[0]
    last=strings[-1]

    for i in range(min(len(first), len(last))):
        if first[i]==last[i]:
            result+= first[i]
        else:
            break
    return result

print(common_prefix(strings))