# Application for shortlisting the candidates for interview using the below shown operators
# 1. AND    2. OR   3. NOT

# 1. Operators- AND

has_learned_python = True
has_degree = True

if has_learned_python and has_degree:
    print("Shortlist Candidate for interview")


# 2. Operators- OR

has_learned_python = True
has_degree = True

if has_learned_python or has_degree:
    print("Shortlist Candidate for interview")


# 3. Operators- NOT

has_learned_python = True
is_working_currently = False

if has_learned_python and not is_working_currently:
    print("Shortlist Candidate for interview")



