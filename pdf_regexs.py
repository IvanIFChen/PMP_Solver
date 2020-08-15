regexs = [
    {
        'target': 1,
        'regexs': [
            # 'PMP Lite Mock Exam' and 'Knowledge Area Quiz'
            # (1044 questions) TODO: didn't confirm
            [r'Test Questions\n([\S\s]*?)Answer Key and Explanations', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        'target': 2,
        'regexs': [
            # 'Practice Questions' (400 questions)
            [r'Practice Questions\n([\S\s]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # 'Practice Test' at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 3,
        'regexs': [
            # 'Practice Questions' (239 questions) TODO: didn't confirm
            [r'\nReview Questions\n([\S\s]*?)(?:Chapter   |Appendix   )', r'\d\. ([\S\s]*?)A\.'],
        ]
    },
    # {
    #     'target': 4,
    #     'regexs': [
    #         # 'Practice Questions' (400 questions)
    #         [r'Practice Questions\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
    #         # 'Practice Test' at the end (200 questions)
    #         [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
    #     ]
    # },
    {
        'target': 5,
        'regexs': [
            # 'Practice Questions' (400 questions)
            [r'Practice Questions\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # 'Practice Test' at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 6,
        'regexs': [
            # 'Review Questions' at the end of each chapter
            # (~187 questions) TODO: didn't confirm
            [r'Review Questions\n([\s\S]*?)(?:CHAPTER|APPENDIX)', r'\d\. ([\S\s]*?)A\.']
        ]
    }
]