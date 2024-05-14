# Introduction

Drone, robotics, automatic controlled vehicle, vehicle tranportation control system in road, weather prediction and control, missile automatic defense system. We need science and engineering for better life or industry. 

We have AI. AI can resolve everything, right? The answer is no. Combination of physics, math and computer science takes important role. In this rep, mainly, some kind of study and small research will be taken by numerical calculation bases. It is supposeod that geometry takes main role and partially, manifold, vector fied and physics own its role. Multi-core CPU or GPU programming would be plus but it is not main argument.

# geometry, manifold, differential and integral.

In this repository, several numerical simulation for geometry and manifold will be impled. OpenGL/GLUT with python will be used for visualization. Why not C++ and OpenGL? It is because it is prototyping and not required to massive number of calculation and REPL cycle would be important compared with particle simulation. If hard numerical calculation is required, the code is transfered to C++.

Remark:
As you can see, in this rep, python is used to program idea of math. However, even calculation order and speed with enough for modern CPU, I recommend univ students to use C or C++ for their calculation. C++ might be obvious if one checked my rep of particle simulation of fluid dynamics. Why C as well? For control of robotics or vehicle, C may be used to calc control input and emit signal via DA converter or even digital control is utilized. It is realtime computing. C may be faster than C++ even C++ is fast enough. Considering ultimate situation, the author recommend to study C++ and C. And use it as training.

Remark:
I am new undergrad univ student. I want to be marketer. So, I don't need to study differential and integral calculus. I want to be psychologist. So, I don't need matrix and calculus. Is it truth? The author thinks it isn't. Both of professisions use several multivariable analysis which is kind of statics, and it uses calculus and linear algebra as bases. Actually, it is possible to claculate using software package such as R for that kind of a statical values. But without having knowledge of math used on bases, deep understanding of analysis would no be made. Thus, the author recommend to study linear albegra and calculus even one's major is not science or engineering.

Differential and integral? For me, it seems it have relationship to geometry especially, if it were visualized. Moreover, for advanced topic, ODE could be expressed by matrix and vector. They may have geometrically meaning.

Line integral is interesting math expression for me. As symbol, it is easy to understand raw meaning, it is difficult to understand numerically and programmary.

For me, combination of geometry and manifold seems close to albegra-geometry in old Japanese high school text.

Applications areas are assumed to be analysis of ODE esp, smart material systems, robotics, automatic controlled vehicle, fluid dynamics, electro-magnetic dynamics and so on.

# Relation of math, physics and computer science

What's line integral? What is vector field analysis? It has relation with fluid dynamics and possibly with electro-magnetic dynamics. Actually, ODE was made with classical mechanics. Without having physical insight, it would not be possible to make ODE and no analysis could not be made. Computer science, esp, search engine and recommendation engine have strong relationship with matematics. Why not education in high school math with example of physics and computer science? OK, no education in high school. But students can study by oneselves with some easy to read text book. The authour is relatively well at physics but mainly, applied mathematician. One could be physics person but math could be done. Whichever, the author recommend to study both.

# Why simple math model especially pendulum for complex applications such as bicyle, vehicle and Smart Material Systems?

Essence is simple. If it were not simple, it is not essence. The major topic or interest of the author is mathematical property or description of dynamics of nonlinear systems especially for smart material systems. It is complex application. However, ultimately, it would goes close to combination of nolinear pendulum and dumper or nonlienar elasticity with multiple variables. This is not application development but study and research of ODE or manifold for Smart Material Systems. To disclose essencial property of nonlienear systems, relatively simple model is utlized to make clear what is nolinear avoiding model complexility. If one have interest for development of application itself, it would be better to go to development of equation for complex systems. But it isn't at this time. The author takes position as applied mathematician without super computer.

# Note on numerical differentiation and education esp. Japanese high school

loop with decreasement of xdot for numerical diff has been impled. In high school analytical diff, it would be ordinary to express diff with line to understand what is differentiation. This is numerical version of that. If a user is not familiar with differentiation, it would be good idea to play with numerical differentiation.

The author thinks that Japanese high school student think too much about technique for exam for entrace of Univs. Memorize formula, memorize past test. But don't think meaning. Is it because of students? The author thinks no. I think it is mistake of Ministry of Education.

Several years before, suddenly, I read past exam of Univ. Tokyo. It seems it is not so difficult. If author is serious about that book, it would be possible to obtain 60% by study from 2nd year of high school. Actually, when I was high school student, I didn't but past exam book of red-book but for centre exam only. It is recommended to go to middle range national university and then, go to Titech or Tsukuba by master. The author is 83% for centre exam, esp. 196/200 for English and 90% over for Physics. TOEFL CBT 233/300 before go to England. First Class (over 70% is A grade) B.Eng and skipped British M.Phil. I think I have right to say about education.

All in all, the author recommend to study real math and physics as I shown in this rep. PC would be expensive for high school student. Do part time job, buy functional calculator and graph-paper. And then, play with algebra, geometry, differeitiation and integration. Physics and ordinary differential equation is plus.

# Ordinary Differential Equation, Partial Differential Equation, FEM, Digital Lagrangian and Micro Mechanics -Math, Physics and Computer Science-

For preparation of study of vector field, numerical simulation of micro-mechanics for fluid dynamics with simple particle prototype is deployed. It is multiple particle and fluid not material or solid state physics. Historically, micro mechanics is used for material engineering but the author thinks that it is also appropriate to model fluid dynamics considering meaning of micro-mechanics. 

Mori-Tanaka's micro mechanics is basically based on disturbance observer. This micro mechanics is based on particle and multiple ODE-solver with python or C++. The difference would be come from the power of programming. It was PDE and analysis. Or even with Hibert Space. For old ages, computer simulation or experiment is not popular and long queue for CPU cluster is required. Thanks to Apple Mx series SoC, now we can calcualte physical phenomia by very fast speed. Metal for GPU or Posix Threads for multi-CPU core would be plus.

Author investigated about material mechanics and thus, some time duration, investigation of fluid would be done by some chunk of times.

# Modelling and mesoscopic physics

We have paticle. We have high speed CPU/GPU. Just implement particle. We don't need physics then? No. Actually, particle is not atom but virtual particle which express some set of molecule of water, air or other fluid. This is assumed to be some mesoscopic physics and virtual physical particle. The author thinks that this is some kind of hypothesis and physical modelling. Although it would be different from ordinary physics, it would be some kind of physics. Hypothesis. The author thinks that is a core of physics.

# Math is dry?

There are arguments such that math is dry and just calculation. I don't think so. Math can expresses how vehicle moves. Using math, aeroplane flys. iPad text? Moving objects? Gaming? Partially agree. I think point is Squeak, processing or Swift Playground. Think math critically, make it as program, visualize, think and analyze. Using iPad may makes student passive, though I think what maker think is correct. Then, you may understand and could feel what is math. Can you enjoy music? The author thinks that's the same.