INSERT INTO Student VALUES 
(3035568324,'Au Cheuk Ying', 'u3556832@connect.hku.hk', NOW(), '2021-01-20', '00:00:00'), 
(3035569720,'Joyce Leung', 'joyce36@hku.hk', NOW(), '2021-01-20', '00:00:00'),
(3035372505,'Lam Wun Yin', 'willyin@hku.hk', NOW(), '2021-01-20', '00:00:00'),
(3035553472,'Liew Van Kie', 'vankie@hku.hk', NOW(), '2021-01-20', '00:00:00'),
(3035549017,'Kathleen Zi Yi Low', 'u3554901@connect.hku.hk', NOW(), '2021-01-20', '00:00:00');

INSERT INTO Classroom VALUES
(1,'RR301'), 
(2,'KB223'), 
(3,'CPD-3.28'), 
(4,'CPD-3.04'), 
(5, 'CYP2'), 
(6, 'MB262'), 
(7, 'ONLINE'),
(8, 'CYC103');

INSERT INTO Teacher VALUES 
(1,'Ping Luo'), 
(2,'Weilerscheid-Fung Tonja'), 
(3,'Li Wentao'), 
(4,'Yin Guosheng'), 
(5, 'Charlie Wong'), 
(6, 'Rocky Law'), 
(7, 'Will Hayward'), 
(8, 'Benise Mak'), 
(9, 'Sing-Hang Cheung'),
(10, 'Jenny Lee'),
(11, 'Oliveira Bruno'), 
(12, 'Choi Yi King'), 
(13, 'Robert David William'),
(14, 'D. Schnieders');

INSERT INTO Course VALUES
('COMP3278', 'Introduction to database management systems', 'Database design, query languages, system design, application development', 'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09', 'Video recording of Lecture 8 has been released.', 2), 
('GRMN3002','German III.2','It offers a balanced range of language skills and furthers exploration of the various linguistic aspects of the language.','https://hku.zoom.us/j/96851353752#success', 'Translation of the text has been uploaded.', 3), 
('STAT3600','Linear statistical analysis', 'Simple linear regression, Multiple linear regression, One-way classification models, Two-way classification models, Universal approach to linear modelling, Regression diagnostics', 'https://hku.zoom.us/j/97512238445?pwd=YUozWjRvTXZjcFNJYUl5V1BoQkEyQT09', 'We will have the midterm exam this Friday, 26 March, from 2:30pm--4:30pm.', 1), 
('STAT3622', 'Data visualization', 'Data science, data manipulation, exploratory data analysis, statistical graphics, interactive data visualization, shiny applications(R), selected case studies.', 'https://hku.zoom.us/j/4455439507', 'Dear All, Please fill the survey via Moodle. Thank you very much.', 4),
('STAT2602', 'Probability and statistics', 'This course builds on STAT2601, introducing further the concepts and methods of statistics. Emphasis is on the two major areas of statistical analysis: estimation and hypothesis testing.  Through the disciplines of statistical modelling, inference and decision making, students will be equipped with both quantitative skills and qualitative perceptions essential for making rigorous statistical analysis of real-life data.', 'https://hku.zoom.us/j/6887247266', 'Next Tutorial will be held on 20/05, 1130~1220.', 5),
('ENTR3001', 'Science-based innovation development', 'This Minor aims at broadening the horizon of our undergraduate students with respect to entrepreneurship, so as to arouse their interest in this aspect and better equip them. It is also important for our students to visualize how their training in science (a) is relevant to the real world and (b) can bring about huge insights via critical analysis of the operation of existing enterprises. With the vivid commercial environment and a growing atmosphere for start-ups both locally and globally, this Minor also serves to offer more competitive edge to our students via connecting their academic knowledge with the real world, even though they may not initiate their own start-ups in the short run.', 'https://zoom.us/j/94984992956?pwd=MkVZZmN5a0J4dTBoZzZtQVdENDRiUT09', 'The Online Evaluation of Teaching and Learning (SETL) for ENTR3001 will be conducted from April 18 to May 17, 2021.', 6),
('PSYC2067A', 'Seminars in cognitive science', 'This course is a tutorial-based reading course in specialist areas of cognitive science research and interest. It will include presentations and group discussion of research and issues of interest within cognitive science, providing an opportunity for students to examine critically the cognitive science approach to understanding intelligent systems.', 'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09', 'Students can expect to receive feedback within 2-3 weeks after submitting written assignments and quizzes. Students can get individual feedback about their assignments through meeting with the course tutor. Weekly consultation hours are set up for individual consultation.', 7),
('PSYC2067B', 'Seminars in cognitive science', 'This course is a tutorial-based reading course in specialist areas of cognitive science research and interest. It will include presentations and group discussion of research and issues of interest within cognitive science, providing an opportunity for students to examine critically the cognitive science approach to understanding intelligent systems.', 'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09', 'Students can expect to receive feedback within 2-3 weeks after submitting written assignments and quizzes. Students can get individual feedback about their assignments through meeting with the course tutor. Weekly consultation hours are set up for individual consultation.', 7),
('PSYC2113A', 'Introduction to Brain Imaging', 'Functional Magnetic Resonance Imaging (fMRI) is widely used to study brain functions. This course is designed to provide a general introduction to the physical and physiological bases and principles of fMRI, MRI related safety issues, and design and analysis of fMRI experiments.', 'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09', 'There will be FOUR 40-minute quizzes (Feb. 22, Mar. 15, Apr. 8 and Apr. 29). The quizzes will cover materials discussed BOTH during lectures and in the assigned readings.', 7),
('PSYC2113B', 'Introduction to Brain Imaging', 'Functional Magnetic Resonance Imaging (fMRI) is widely used to study brain functions. This course is designed to provide a general introduction to the physical and physiological bases and principles of fMRI, MRI related safety issues, and design and analysis of fMRI experiments.', 'https://hku.zoom.us/j/97686555806?pwd=NWxSNVRKTlNDU0NjYTgremxaQ3pldz09', 'There will be FOUR 40-minute quizzes (Feb. 22, Mar. 15, Apr. 8 and Apr. 29). The quizzes will cover materials discussed BOTH during lectures and in the assigned readings.', 7),
('COMP3259', 'Principles of programming languages', 'This course covers central concepts in programming languages, language design and implementation, and programming paradigms.The course will have a practical focus, encouraging students to implement a progressively more sophisticated programming language illustrating various concepts and ideas from functional, imperative and object-oriented programming. These concepts include for example static scoping, closures, inheritance, mutable state, and type systems. All such features are widely used by many existing programming languages.', 'https://hku.zoom.us/j/94663759273?pwd=WktuNUlRbDVhaVhUSFUwSEFBR0tNZz09', 'Upcoming quiz will be held on 15/4.', 7),
('COMP3359', 'Artificial Intelligence Applications', 'This course focuses on practical applications of AI technologies. The course comprises two main components: students first acquire the knowledge and know-how of the state-of-the-art AI technologies, platforms and tools (e.g., TensorFlow, PyTorch, Open AI, scikit-learn, Azure AI) via self-learning of designated materials including open courseware. Students will then explore practical AI applications and complete a course project which implements an AI-powered solution to a problem of their own choice.', 'NIL', 'Please form groups of 4 for the final project.', 8),
('FREN3002', 'French III.2', 'This course is a continuation of French III.1.  The intention is to further expand students’ proficiency in French.  Class lectures will make use of interactive approaches so as to elicit creativity, problem-solving skills, and to encourage participants to become independent users of the language.  Various literary and non-literary texts from France and other French-speaking countries will be used, with the aim of stimulating critical reading and discussion.', 'https://hku.zoom.us/j/91907715959?pwd=V1Mya3htbzBReFlBMFZTRXhGdlREQT09', 'Bonjour! The vocabulary test will be held on next Tuesday.', 7),
('COMP3270', 'Artificial intelligence', 'This is an introduction course on the subject of artificial intelligence. Topics include: intelligent agents; search techniques for problem solving; knowledge representation; logical inference; reasoning under uncertainty; statistical models and machine learning. This course may not be taken with BUSI0088.', 'https://hku.zoom.us/j/95520444229?pwd=Y243RldCUDJMQndkYUx4aXBoQkpyZz09', 'We have posted the materials on Moodle. Please check it out.', 7);

INSERT INTO `Course_materials` VALUES 
('COMP3278','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'), 
('GRMN3002','https://drive.google.com/file/d/17Hvw1T03C6nmFGJDqFG5Q3JICpsj5IYq/view?usp=sharing'), 
('STAT3600','https://drive.google.com/file/d/1jsFf1H4uZXc496lDhdoUonMKHg5KSHyW/view?usp=sharing'), 
('STAT3622','https://drive.google.com/file/d/1jsEDxkXMSA84soE-doILXKPTvA9U6IsE/view?usp=sharing'),
('STAT2602','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('ENTR3001', 'https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('PSYC2067A','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('PSYC2067B','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('PSYC2113A','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('PSYC2113B', 'https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('COMP3259','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('COMP3359','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('FREN3002','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing'),
('COMP3270','https://drive.google.com/file/d/19zlAwptJGyfQYhBsa1l8r8sw3lJ_-6MX/view?usp=sharing');

INSERT INTO `Course_timeslots` VALUES
('COMP3278', 'TUE 0930 - 1030'),
('COMP3278', 'FRI 0930 - 1130'),
('GRMN3002', 'MON 0930 - 1130'),
('GRMN3002', 'THU 0930 - 1030'),
('STAT3600', 'FRI 1430 - 1730'),
('STAT3622', 'MON 1430 - 1730'),
('STAT2602', 'TUE 1330 - 1630'),
('ENTR3001', 'MON 1430 - 1730'),
('PSYC2067A', 'MON 0930 - 1130'),
('PSYC2067B', 'MON 1130 - 1230'),
('PSYC2113A', 'MON 1530 - 1630'),
('PSYC2113B', 'THU 1530 - 1630'),
('COMP3259', 'MON 1430 - 1530'),
('COMP3259', 'THU 1330 - 1530'),
('COMP3359', 'MON 0930 - 1130'),
('COMP3359', 'THU 0930 - 1030'),
('FREN3002', 'MON 1230 - 1430'),
('FREN3002', 'FRI 1230 - 1430'),
('COMP3270', 'MON 1430 - 1530'),
('COMP3270', 'THU 1330 - 1530');

INSERT INTO takes VALUES 
(3035568324, 'COMP3278'), 
(3035568324, 'STAT3600'), 
(3035568324, 'GRMN3002'), 
(3035568324, 'STAT3622'),
(3035549017, 'STAT2602'),
(3035549017, 'ENTR3001'),
(3035553472, 'PSYC2067A'),
(3035553472, 'PSYC2067B'),
(3035553472, 'PSYC2113A'),
(3035553472, 'PSYC2113B'),
(3035569720, 'COMP3259'),
(3035569720, 'COMP3278'),
(3035569720, 'COMP3359'),
(3035569720, 'STAT2602'),
(3035569720, 'FREN3002'),
(3035372505, 'COMP3270');

INSERT INTO teaches VALUES 
('COMP3278', 1), 
('GRMN3002', 2), 
('STAT3600', 3), 
('STAT3622', 4), 
('STAT2602', 5),
('ENTR3001', 6),
('PSYC2067A', 7),
('PSYC2067B', 8),
('PSYC2113A', 9),
('PSYC2113B', 10),
('COMP3259', 11),
('COMP3359', 12),
('FREN3002', 13),
('COMP3270', 14);
