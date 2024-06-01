# Micro mechanics approach to fluid dynamics. Simple to Complex


When I was under grad student, I studied fluid dynamics and thermo dynamics. There were PDE. How is it analysed? Harmonic analysis? So what? I know about FEM but I thought it is just calculation. What can be known by just calculation? Then, I stopped to study fluid dynamics.

Now, I know the power of numerical calculation and hypotheis driven. I studied and researched enough amount of control engineering and material mechanics. Then, I think it is good timing to study and reserch fluid dynamics.

Micro-mechanics. Mid of micro molecular and macro model. Theoritically, even atom could be modelled. When I was 4th year, I joined to CFRP research group of Univ Tsukuba. In that time, Mori-Tanaka's micro mechanics and related field is assigned to me as a base for research. In that time, because of my misunderstanding, I thought, it is macro model and boaring. Professor's desiction to treat micro-mechanics by me is correct.

Thermo dynamics? How to interact thermo effect with particle? Suppose thermo is transffered to a particle and that energy is partially converted to kinetic energy;i.e. $T(E) = 1/2 mv^2$. Thus, $v = \sqrt(T(E) * 2/m)$.

Moreover, the author suppose that it would be possible to model CFRP or metal material by this methodology. Make strong gravity and then, each particle is bonded. It is not fluid anymore but solid state. The author supposes that this hypothesis is worth to investigate.

Micro mechanics can handle gravity, ion-bonding, H2-Bonding, electric field and so on. Micro to Mesoscopic can also be handled. It seems most model of mechanical engineering can be modeled by this framework. The interesting point is to modelling micro ODE and several forces, and relation of particles, macro behaviour can be observed by computer simulation and possibly, to be analyzed if it were close to system matrix, though the author thinks computer simulation is better choice.

The author thinks micro-mechanics is simple and easy to treat and can model complex system, material and fluid. Digital lagrangian is good for analysis esp. for control engineering. I think micro-mechanics is good for numerical simulation. And modelling is straight forward, concise and easy to understands as a natural extension of classical mechanics.

In this report and repository, some kind of study and reserach will be taken. The methodolody is assumed to be hypothesis driven physical modelling and micro-mechanics apparoch and visualizing with numerical simulation using Python and OpenGL/GLUT.

It could be said that C++ is faster than Python. However, considering educational effect and openness to every one, Python would be utilized.

# Aim, Objective and Methodology

## Aim
- Understanding characteristics of fluid dynamics, better applications of fluid dynamics will be made;i.e. better vehicle, better drone, better aeroplane. They have impact to real life.

## Objective
- To make an easy to use and implementable simulator;
- To understand fluid dynamics with easy to use simulator;
- To make method of control of fluid dynamics via micro mechanical method.

## Methodology
- Numerical simulation based visualization of particles and trajectry analysis using frequency domain analysis, geometry and physics.

# Differential Equation and applications

Vehicle. Aeroplane. Drone. There are many applications in industry which require fluid dynamics for research. In this rep, micro mechanical methodology is taken to modelling of fluid and mainly, vehicle or bycle as a application, simulation would be taken. Ultimately, it would be shown that air-flow with some shape of disk-wheel or composite-wheel, it would be make flow of air better for high performance of vehicle and bicycle. Drone dev could deploy this simulator to research/study their fluid.

# Order of calculation. LL and C++

Numerical simulation environment:
- CPU: Apple M1 2020
- Memory: 16GB
- Programming Language: Python 3.9.X
- Graphic Library: OpenGL, GLUT and their Python binding

It works. This OO simulator works. Lego-blocking approach of component is fun and high productivity. In this first version of simulator with Simple Particle, 100 or 200 particle are max and it is not possible to do real time rendering by 1000 particles. It is assumed to be 3 reasons.

1. order of calc with simple particle manager. All particle has effect from all particles which is $O(n^2)$.
2. Particles require many call of vertex which is open GL function to render circle. Polygon might be enough.
3. Multi core processing. It seems that python could be used by multi core processing by some method.
4. Cython? Final option.

Someone could argue that MacBook Pro and M4Max would be better choice. It could be but I think it could be different. Ultimately, numerical calculation could be more than 1 week to calc. In that time, mac studio or server is better choice. If it were less than 5 min or real time, it is OK to use pro. However, I suppose to use combination of MacbookAir and studio or GPU cluster on AWS would be better choice.

# Research log

It is interesting too see trajectory of particle with different class of differential equation. If there are dumper, it goes to origin.

Setting of num calc has been changed. The more particle and the more far ortho, it gets close to particle. Around 200 particles may be limit by python. Is it should be C++ or split simulator and visualizer to different program? The author thinks several bottle neck of this simular is better to be resolved such as order of particle manager.

It seems there are equibrium for enought number of particles and thus, not so much oscillation.

## Simple 100 Particles with reflection hypothesis

![100 particles with reflection](/articles/img/si-100.png "100 particles with reflection")

In this figure, it is shown that if there are many particle, they are on equilibrium and not moved their relative position. It might be as a result of spring type ODE per particle and gravity with particle to particle.

It would be said that it is close to real water since which has H-bonding with $H_2O$ melecular. The more particles, the more close to molecular and then, it make some of cells in micro mechanics or solid state physics and then, goes to equibrium.

It might be interesting to see the effect of amplitude of gravity. If they goes to higher, it would be close to solid material. If not, it would be close to be liquid or even air.
