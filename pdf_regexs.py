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
        # ##### By Dani #####
    {
        # 1
        'target': '200_PMP_Sample_Questions_Bn6th',
        'regexs': [
            # Total 'QUESTION's : 1004 - 99 (same) = 905 questions
            [r'\n\s*Questions([\S\s]*?)\n\s*Answers and References', r'\d\. ([\S\s]*?)\d*\s+o ']
        ]
    },
    {
        # 2
        'target': 'CAPM_In_Depth_-_Certified_Associate_in_Project_Management_Study_Guide_for_the_CAPM_Exam_2011_Bn4th',
        'regexs': [
            # 'Review Questions' at the end of each chapter (153 questions)
            [r'Review Questions\n([\s\S]*?)(?:\nChapter|\nAppendix)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 3
        'target': 'CAPM_PMP_Project_Management_All-in-One_Exam_Guide_2007',
        'regexs': [
            # 'Questions' at the end of each chapter (260 questions)
            [r'Questions\n([\s\S]*?)Answers\n', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 5
        'target': 'CertChamp_PMP_6_Mock_Test_Bn6th',
        'regexs': [
            # Total 'QUESTION's : 1004 - 99 (same) = 905 questions
            [r'\nQuestion - ([\S\s]*?)\n\w is the correct answer.', r'\d\n([\S\s]*?)A\.']
        ]
    },
    {
        # 6
        'target': 'EdWel_PMP_Exam_Preparation_Bootcamp_Participant_Manual_2_6_Online_Free_Bn4th',
        'regexs': [
            # 'Review Questions' at the end of chapter 2~12 (271 questions)
            # Chapter 2 Test & Chapter 2 Test Answers
            # Chapter 3 Test & Chapter 3 - Test Answers
            # Chapter 4 Test & Chapter 4 Test - Answers (same: chapter 6, 7, 8, 11, 12)
            # Chapter 5 - Test & Chapter 5 Test - Answers
            # Chapter Nine Test & Chapter 9 Test - Answers
            # Chapter 10 Test & Chapter 10 - Answers
            # [r'Chapter (\S)+ (- )*Test\n([\S\s]*?)Chapter (\S)+(Test )*(- )*Answers\n', r'\d\. ([\S\s]*?)a\.']
            [r'Chapter 2 Test\n([\S\s]*?)Chapter 2 Test Answers\n', r'\d\. ([\S\s]*?)a\.'],
            [r'Chapter 3 Test\n([\S\s]*?)Chapter 3 - Test Answers\n', r'\d\. ([\S\s]*?)a\.'],
            [r'Chapter (?:4|6|7|8|11|12) Test\n([\S\s]*?)Chapter (?:4|6|7|8|11|12) Test - Answers\n', r'\d\. ([\S\s]*?)a\.'],
            [r'Chapter 5 - Test\n([\S\s]*?)Chapter 5 Test - Answers\n', r'\d\. ([\S\s]*?)a\.'],
            [r'Chapter Nine Test\n([\S\s]*?)Chapter 9 Test - Answers\n', r'\d\. ([\S\s]*?)a\.'],
            [r'Chapter 10 Test\n([\S\s]*?)Chapter 10 - Answers\n', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        # 8
        'target': 'PMI.ActualTests.PMI-001.v2013-08-27.by.Smartadmin.1005q_Bn5th',
        'regexs': [
            # Total 'QUESTION's : 1004 - 99 (same) = 905 questions
            [r'\nQUESTION ([\S\s]*?)\nCorrect Answer', r'\d\n([\S\s]*?)A\.']
        ]
    },
        # 9 TODO: Something wrong
        # 10 TODO: Something wrong (give up)
    {
        # 17
        'target': 'PMP_Project_Management_Professional_Exam_Study_Guide_8th_2016_Bn5th',
        'regexs': [
            # Assessment Test (72 questions)
            [r'\nAssessment Test\n(1\.[\s\S]*?)Answers to Assessment Test', r'\d\. ([\S\s]*?)A\. '],
            # Review Questions (~240 questions)
            [r'\nReview Questions\n([\s\S]*?)(?:\nCHAPTER|\nAppendices)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 18
        'target': 'PMP_Project_Management_Professional_Exam_Study_Guide_9th_2018_Bn6th',
        'regexs': [
            # Assessment Test (77 questions)
            [r'\nAssessment Test\n(1\.[\s\S]*?)Answers to Assessment Test', r'\d\. ([\S\s]*?)A\. '],
            # Review Questions (~240 questions)
            [r'\nReview Questions\n([\s\S]*?)(?:\nChapter   |\nAppendix   )', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 19 TODO: Something wrong
        'target': 'PMP_Project_Management_Professional_Practice_Tests_2018_Bn6th',
        'regexs': [
            # Questions at the end of each chapter (1001 questions)
            # Missing 1st question of each chapter but chapter 1 and others
            # Total questions are 986 questions.
            # [r'(?:\n1. | 1. )([\s\S]*?)(?:Chapter   \w|\nAnswers Appendix\n)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 20
        'target': 'PMP_Project_Management_Professional_Review_Guide_Updated_for_the_2015_Exam_Bn5th',
        'regexs': [
            # Review Questions (110 questions)
            [r'\nReview Questions\n([\s\S]*?)(?:\nChapter   |\nAppendix   )', r'\d\. ([\S\s]*?)A\.']
        ]
    },
        {
        # 21
        'target': 'PMP_Project_Management_Professional_Study_Guide_3rd_2005_Bn3rd',
        'regexs': [
            # 'Review Questions' at the end of each chapter (240 questions)
            [r'Review Questions\n([\S\s]*?)Answers to Review Questions\n', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 22
        'target': 'PMP_Question_Bank_-_400_PMP_Sample_Questions_2018_Bn6th',
        'regexs': [
            # 'Practice Questions' (400 questions)
            [r'    Practice Questions([\S\s]*?) Answers Sheet', r'Question\: \d*\n([\S\s]*?)\n\(a\)']
        ]
    },
    {
        # 23
        'target': 'PMP_Question_Bank_2004',
        'regexs': [
            # Question Set 1 & 1. & A.|A)|a) & Question Set 2 (117 questions)
            # There are 8 subsets in Question Set 1
            # Question Set 2 & 1. & A. & ANSWERS (200 questions)
            # Question Set 3 & 1. & A. & Answers  (same: set 5, 6) (75 + 220 + 240 questions)
            # Question Set 4 & 1 & A & ANSWERS (50 questions)
            # Question Set 7 & 1. & (1.   |1   ) & Project Management Areas (200 questions)
            # Question Set 8 & 1. & A.|a)|a.|1)|1.|      A |A)|(A)|A:|A : & Question Set 9 (141 questions)
            # Question Set 9 & 1. & A. & "1. B. Bottom up estimating" (100 questions)
            # Question Set 10 & 1. & a. & ANSWERS (100 questions)
            # Total questions are 1,393 questions but catched 1,121 questions
            [r'Question Set 1\n([\S\s]*?)Question Set 2\n', r'\d\. ([\S\s]*?)(?:A\.|A\)|a\))'],
            [r'Question Set 2\n([\S\s]*?)ANSWERS\n', r'\d\. ([\S\s]*?)A\.'],
            [r'Question Set (?:3|5|6)\n([\S\s]*?)Answers\n', r'\d\. ([\S\s]*?)A\.'],
            [r'Question Set 4\n([\S\s]*?)ANSWERS\n', r'\d\. ([\S\s]*?)(?:1.   |1   )'],
            [r'Question Set 7\n([\S\s]*?)Project Management Areas\n', r'\d\. ([\S\s]*?)A\.'],
            [r'Question Set 8\n([\S\s]*?)Question Set 9\n', r'\d\. ([\S\s]*?)(?:\n\s+[Aa1][\.\)\:]?)'],
            [r'Question Set 9\n([\S\s]*?)1. B. Bottom up estimating\n', r'\d\. ([\S\s]*?)A\.'],
            [r'Question Set 10\n([\S\s]*?)ANSWERS\n', r'\d\. ([\S\s]*?)a\.'],
        ]
    },
    {
        # 24
        'target': 'PMP_Review_Exam_Guide_2014_Bn3rd',
        'regexs': [
            # 'Questions' at the end of each chapter (280~283 questions)
            [r'Questions\n([\S\s]*?)Questions and Answers\n', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 25
        'target': 'PMP_in_Depth_-_Project_Management_Professional_Certification_Study_Guide_for_the_PMP_Exam_3rd_2019_Bn6th',
        'regexs': [
            # 'Review Questions' at the end of each chapter
            # (179~187 questions, 8 same questions) TODO: didn't confirm
            [r'Review Questions\n([\s\S]*?)(?:CHAPTER|APPENDIX)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 26
        'target': 'PMP_in_Depth_-_Project_Management_Professional_Study_Guide_for_PMP-CAPM_Exams_2006_Bn3rd',
        'regexs': [
            # 'Review Questions' at the end of each chapter (107 questions)
            [r'Review Questions\n([\s\S]*?)(?:\nChapter|\nAppendix)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 27
        'target': 'PMP_in_Depth_-_Project_Management_Professional_Study_Guide_for_the_PMP_Exam_2010_Bn4th',
        'regexs': [
            # 'Review Questions' at the end of each chapter (165 questions)
            [r'Review Questions\n([\s\S]*?)(?:\nChapter|\nAppendix)', r'\d\. ([\S\s]*?)A\.']
        ]
    },
    {
        # 28 TODO: Something wrong
        'target': 'Preparing_For_The_Project_Management_Professional_PMP_Certification_Exam_3rd_2005_Bn3rd',
        'regexs': [
            # 'Practice Questions' at the end (200 questions)
            # [r'\n  PRACTICE\n QUESTIONS\n([\s\S]*?)PRACTICE QUESTIONS\n   ANSWER KEY', r'\d\. ([\S\s]*?)a\.']
        ]
    },
    {
        # 29
        'target': 'Project_Management_Professional_Exam_PMP_2003',
        'regexs': [
            # Total 'Question's : 1000 (catched 913) questions
            [r'\nQuestion ([\S\s]*?)\nAnswer: ', r'\d\n([\S\s]*?)A\.']
        ]
    },
]