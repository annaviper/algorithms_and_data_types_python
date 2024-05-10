def array_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1 & set2
    return sorted(list(intersection))


def non_repeating_elements(nums):
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    return list(seen - repeated)


def unique_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique_to_1 = sorted(list(set1 - set2))
    unique_to_2 = sorted(list(set2 - set1))
    return unique_to_1, unique_to_2


def find_unique_string_in_list(words):
    seen = set()
    duplicates = set()

    for word in words:
        if word in seen:
            duplicates.add(word)
        seen.add(word)

    for word in words:
        if word not in duplicates:
            return word

    return ""


def anagram_pairs(list_1, list_2):
    """Identify all pairs of anagrams where each pair
    is made up of one word from the first list and one from the second list"""
    sorted_tuples_1 = set(tuple(sorted(word)) for word in list_1)
    sorted_tuples_2 = set(tuple(sorted(word)) for word in list_2)

    common_tuples = sorted_tuples_1 & sorted_tuples_2

    # contains anagrams from the first list
    list_1_output = [word for word in list_1 if
                     tuple(sorted(word)) in common_tuples]
    # contains anagrams from the second list
    list_2_output = [word for word in list_2 if
                     tuple(sorted(word)) in common_tuples]

    output = []
    for word1 in list_1_output:
        for word2 in list_2_output:
            # traversing every pair of words in filtered lists
            if tuple(sorted(word1)) == tuple(sorted(word2)):
                # If words in the pair are anagrams, add them to the output list
                output.append((word1, word2))
    return output
