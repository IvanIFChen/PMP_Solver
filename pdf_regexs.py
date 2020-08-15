regexs = [
    {
        'target': 'PMP_Exam_Prep_Questions_Answers_-_Explanations_Bn6th',
        'regexs': [
            # 'PMP Lite Mock Exam' and 'Knowledge Area Quiz'
            # (1044 questions) TODO: didn't confirm
            [r'Test Questions\n([\S\s]*?)Answer Key and Explanations', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        'target': 'PMP_Exam_Preparation_-_Test_Questions_Practice_Test_and_Simulated_Exam_2019_Bn6th',
        'regexs': [
            # 'Practice Questions' (400 questions)
            [r'Practice Questions\n([\S\s]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # 'Practice Test' at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 'PMI-ACP_Project_Management_Institute_Agile_Certified_Practitioner_exam_study_guide_2018',
        'regexs': [
            # 'Practice Questions' (239 questions) TODO: didn't confirm
            [r'\nReview Questions\n([\S\s]*?)(?:Chapter   |Appendix   )', r'\d\. ([\S\s]*?)A\.'],
        ]
    },
    # {
    #     'target': 'PMP_Exam_Practice_Test_and_Study_Guide_Ninth_Edition_2013_Bn5th',
    #     'regexs': [
    #         # 'Practice Questions' (400 questions)
    #         [r'Practice Questions\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
    #         # 'Practice Test' at the end (200 questions)
    #         [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
    #     ]
    # },
    {
        'target': 'PMP_Exam_Practice_Test_and_Study_Guide_Tenth_Edition_2016_Bn5th',
        'regexs': [
            # 'Practice Questions' (400 questions)
            [r'Practice Questions\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.'],
            # 'Practice Test' at the end (200 questions)
            [r'\nPractice Test\n\n([\s\S]*?)Answer Sheet', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        'target': 'CAPM_in_Depth_2019_Bn6th',
        'regexs': [
            # 'Review Questions' at the end of each chapter
            # (~187 questions) TODO: didn't confirm
            [r'Review Questions\n([\s\S]*?)(?:CHAPTER|APPENDIX)', r'\d\. ([\S\s]*?)A\.']
        ]
    }
]