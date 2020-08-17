regexs = [
    {
        'target': 'PMP_Exam_Prep_Questions_Answers_-_Explanations_Bn6th',
        'regexs': [
            # 'PMP Lite Mock Exam' and 'Knowledge Area Quiz'
            # (1044 questions)
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
            # 'Practice Questions' (239 questions)
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
            # (~187 questions)
            [r'Review Questions\n([\s\S]*?)(?:CHAPTER|APPENDIX)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        'target': 'PMP_Exam_Prep_Questions_Answers_-_Explanations_1000_PMP_Practice_Questions_with_Detailed_Solutions_Bn5th',
        'regexs': [
            # (1024) Questions
            [r'(?:Test |Practice\n)Questions\n([\s\S]*?)\n\nAnswers', r'\d\. ([\S\s]*?)A\. ']
        ]
    },
    {
        'target': 'PMP_Exam_Simplified_Bn5th',
        'regexs': [
            # Sample Questions (65 questions)
            [r'\nQuick Review - Sample Questions([\s\S]*?)Quick Review - Solutions', r'\d\. ([\S\s]*?)a\. '],
            # Sample Test (196 questions)
            [r'FULL SAMPLE\s*?TEST([\s\S]*?)Solutions\n', r'A\d{3}\. ([\S\s]*?)a\. ']
        ]
    },
    {
        'target': 'PMP_Project_Management_Professional_Exam_Study_Guide_5th_2009_Bn4th',
        'regexs': [
            # Assessment Test (70 questions)
            [r'\nAssessment Test\n(1\.[\s\S]*?)Answers to Assessment Test', r'\d\. ([\S\s]*?)A\. '],
            # Review Questions (239 questions)
            [r'\nReview Questions([\s\S]*?)\nAnswers to Review Questions', r'\d\. ([\S\s]*?)A\. ']
        ]
    },
]