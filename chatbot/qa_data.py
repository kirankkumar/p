# study_qa = {
#     "what is ela": "English Language Arts. It encompasses the study of the English language, including reading, writing, speaking, and listening. ELA is a core subject in most schools and is essential for developing strong communication skills.",
#     "what are all the pronouns": "Personal pronouns: Subject pronouns (I, you, he, she, it, we, you, they) and Object pronouns (me, you, him, her, it, us, you, them).Possessive pronouns: (mine, yours, his, hers, its, ours, yours, theirs).Demonstrative pronouns: (this, these, that, those).Relative pronouns: (who, which, that, as).Indefinite pronouns: (each, all, everyone, either, one, both, any, such, somebody).Interrogative pronouns: (who, which, what).Reflexive pronouns: (myself, herself)..",
#     # ... rest of your dictionary entries ...
# }
study_qa = {
        "what is ela": "English Language Arts. It encompasses the study of the English language, including reading, writing, speaking, and listening. ELA is a core subject in most schools and is essential for developing strong communication skills.",
        "what are all the pronouns": "Personal pronouns: Subject pronouns (I, you, he, she, it, we, you, they) and Object pronouns (me, you, him, her, it, us, you, them).Possessive pronouns: (mine, yours, his, hers, its, ours, yours, theirs).Demonstrative pronouns: (this, these, that, those).Relative pronouns: (who, which, that, as).Indefinite pronouns: (each, all, everyone, either, one, both, any, such, somebody).Interrogative pronouns: (who, which, what).Reflexive pronouns: (myself, herself)..",
        "what are context clues": "Context clues are hints and extra information in a sentence or passage that help you understand the meaning of an unknown word. Context clues essentially let you learn new words without outside assistance, like from a teacher or dictionary..",
        "what are nouns": "Common nouns are general names for people, places, things, animals, events, and the like. They begin in lowercase letters..",
        "what are proper nouns": "Proper nouns are specific names given to common nouns. They always begin with a capital letter..",
        "what are nonrestrictive elements": "In contrast to a restrictive element, a nonrestrictive element is word, phrase, or dependent clause that provides added (though not essential) information to a sentence but does not limit (or restrict) the element it modifies..",
        "what are intensive pronouns": "An intensive pronoun is a pronoun that is used to place special emphasis on another noun or pronoun",
        "what are the top 5 figures of speech": "Hyperbole: Used to overstate or emphasize a concept.Metaphor: Compares two unrelated things to create a vivid image.Simile: Compares two things using the words 'like' or 'as'.Personification: Gives human qualities to nonhuman things. Symbol: Represents ideas or concepts through visual or verbal elements.",
        "what are the ethical implications of the characters actions": "The ethical implications of a character's actions can be complex and multifaceted. Societal norms, personal morality, and virtue ethics all play a role in shaping a character's ethical dilemmas.",
        "how does the author create suspense in the narrative": "Authors create suspense in a narrative by: Posing a question, problem, or mystery at the beginning of the book. Divulging more about it as the plot progresses. Carefully withholding and releasing information to the reader..",
        "what are prime numbers": "Prime numbers are natural numbers greater than 1 that have exactly two factors 1 and the number itself. This means that a prime number is only divisible by 1 and itself.",
        "what are composite numbers": "In math, composite numbers can be defined as numbers that have more than two factors.",
        "what is multiplication": "Multiplication is one of the four basic arithmetic operations. It involves repeated addition of groups of equal sizes: When you combine equal groups of objects, multiplication gives you the total number of objects.",
        "what is division": "Division is a mathematical operation that involves sharing an amount into equal-sized groups.",
        "what is addition": "Addition is a process of combining two or more numbers.",
        "what is subtraction": "Subtraction is the operation of finding the difference between two numbers or quantities.",
        "what are fractions": "Fractions represent parts of a whole or collection of objects. Consist of a numerator (number on top) and a denominator (number below the line).",
        "what are decimals": "Decimals are numbers that are not whole. They consist of a whole part and a fractional part, and represent values that lie between integers.",
        "what are percentages": "Percentages represent an amount out of 100. Can be calculated by dividing a number by the whole and multiplying by 100. Provide a consistent base for comparing fractional parts. Are often denoted by the symbol '%'.",
        "what are integers": "Integers are: The collection of whole numbers and negative numbers. Numbers that can be positive, negative, or zero, but cannot be a fraction. Represented by the symbol 'Z'. Include all whole numbers and negative numbers without fractions and decimals.",
        "what is geometry": "The branch of mathematics concerned with the properties and relations of points, lines, surfaces, solids, and higher dimensional analogs.",
        "what is algebra": "Algebra is the part of mathematics that helps represent problems or situations in the form of mathematical expressions.",
        "what is distributive property": "The distributive property is a fundamental property that defines how multiplication operation is distributed over addition and subtraction.",
        "what is associative property": "The associative property in mathematics applies to addition and multiplication. Rearranging the parentheses in an expression will not change the result. The way in which numbers are grouped by brackets (parentheses) does not affect their sum or product. The sum or product of three or more numbers can be performed in any order. The property does not apply to subtraction and division.",
        "what is commutative property": "The commutative property is a mathematical property that applies to addition and multiplication",
        "what is mean": "The mean is a type of average. It is the total sum of all the numbers in the set, then divided by how many numbers are in the set.",
        "what is median": "The median is a metric used in statistics. It is the middle number in a sorted ascending or descending list of numbers.",
        "what is mode": "The mode is the value that appears most often in a set of data. The mode of a discrete probability distribution is the value x at which its probability mass function takes its maximum value. In other words, it is the value that is most likely to be sampled.",
        "what is range": "The range in mathematics refers to the difference between the lowest and highest values in a set of numbers."
    }

# Optional: Keep the original console version
def study_chatbot():
    print("Hello! I am your Study Answer Chatbot.")
    print("I can answer questions about ELA, Math, Literary Analysis, and Statistics!")
    print("Type 'exit' to quit.\n")

    while True:
        user_input = input("Ask your question: ").strip().lower()

        if user_input == 'exit':
            print("Goodbye! Keep exploring!")
            break

        user_input = ' '.join(user_input.split())
        user_input = user_input.rstrip('?.')

        answer = study_qa.get(user_input, "I'm sorry, I don't know the answer to that question. Please try asking something else.")
        print(f"\n{answer}\n")

if __name__ == "__main__":
    study_chatbot()