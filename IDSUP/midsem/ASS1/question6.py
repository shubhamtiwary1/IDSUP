#Name : Priyansu Nagchowdhary
#Reg. no. : 2141014004
def find_duplicates(input_list):
    seen = set()
    duplicates = set()
    for item in input_list:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

def main():
    StringList1 = input("Enter a list of strings separated by spaces: ").split()
    MStringList1 = find_duplicates(StringList1)
    print("MStringList1:", MStringList1)
    for item in MStringList1:
        occurrence_count = StringList1.count(item)
        print(f"{item} occurs {occurrence_count} {'even' if occurrence_count % 2 == 0 else 'odd'} number of times.")
    word_to_remove = input("Enter the word to remove from StringList1: ")
    if StringList1.count(word_to_remove) >= 2:
        index_to_remove = StringList1.index(word_to_remove, StringList1.index(word_to_remove) + 1)
        del StringList1[index_to_remove]
        print("StringList1 after removing the second occurrence of", word_to_remove + ":", StringList1)
    else:
        print("The word does not occur at least twice in StringList1.")

if __name__ == "__main__":
    main()
