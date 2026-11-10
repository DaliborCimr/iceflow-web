---
title: The story of IceFlow
description: How one person built a deep online hockey manager in seven months - almost entirely through conversations with AI.
lead: >-
  IceFlow is a solo project. Apart from some Photoshop work on the graphics, about 99 % of it
  was created through conversations with artificial intelligence - most of them on walks with a
  baby stroller. It took no free time away, and still a complete product came out of it. The point
  was to show what one person with the right knowledge can build today.
stats:
  - value: '1'
    label: developer
  - value: '7'
    label: months, April to November 2026
  - value: '4'
    label: repositories - engine, server, app, animation editor
  - value: '1,700+'
    label: commits
  - value: '~256,000'
    label: lines of code
  - value: '10'
    label: languages
timelineTitle: How the game grew
milestones:
  - date: April 2026
    phase: idea
    phaseLabel: Idea
    title: Just talking to AI
    text: >-
      No code yet. Walks with the stroller turned into long conversations with AI about what a
      mobile hockey manager should be: live coaching, players who develop over a career, a
      persistent online world and a fair economy.
  - date: 27 April 2026
    phase: engine
    phaseLabel: Match engine
    title: First match engine prototype
    text: >-
      A Python prototype simulates a hockey game period by period: shifts, line changes, zone
      play and goals. It becomes the lab where the rules of the game are tuned.
  - date: May 2026
    phase: engine
    phaseLabel: Match engine
    title: Depth in the simulation
    text: >-
      Advanced statistics, goalies, score-state effects and match form. The engine is refactored
      and calibrated until the numbers start to look like real hockey.
  - date: Early June 2026
    phase: engine
    phaseLabel: Match engine
    title: General manager and economy
    text: >-
      The prototype grows a GM module: salaries, facility maintenance, match income, fatigue and
      injuries, with a cash economy that has to hold up over many seasons.
  - date: 10 June 2026
    phase: server
    phaseLabel: Server
    title: The online server is born
    text: >-
      The real game server starts in Kotlin and Quarkus with PostgreSQL: club generator, training
      progression and, four days later, a full simulated league season.
  - date: Late June 2026
    phase: mobile
    phaseLabel: Mobile app
    title: The mobile app and the transfer market
    text: >-
      The Flutter app starts on 24 June, with translations into other languages just two days
      later. On the server: junior scouting, the transfer market, Redis, facilities, and team
      lines and tactics.
  - date: July 2026
    phase: server
    phaseLabel: Server
    title: The busiest month
    text: >-
      Around 600 commits across server and app. Playoffs, a real-time market pushed over SSE,
      sponsors, nationalities, club logos and kit colours, the Elite cup, the arena, bot clubs and
      the Python match form ported into the server engine.
  - date: August 2026
    phase: animation
    phaseLabel: Animation
    title: Live match and animations
    text: >-
      A live-match preview mode appears, followed by in-match changes to lineups, tactics and the
      goalie. On 24 August a separate animation editor is born, and its goal celebrations land in
      the app the same day.
  - date: September 2026
    phase: server
    phaseLabel: Server
    title: Making it hold together online
    text: >-
      One shared server clock, no club changes while its match is on the ice, a bot runner for
      load, deadlock fixes, faster queries and the farm competition in the app.
  - date: October 2026
    phase: engine
    phaseLabel: Match engine
    title: Calibration, tutorial and fair monetisation
    text: >-
      The engine is recalibrated against NHL numbers and tactics follow a sourced charter. The
      tutorial and registration arrive, then the Stars currency, daily and season tasks, the Rapid
      league, the star store and 25 lifetime achievements.
  - date: Early November 2026
    phase: launch
    phaseLabel: Launch prep
    title: Getting ready for launch
    text: >-
      67 new live-match animations, player mentality, discipline and form, match importance from
      the real table, Sign in with Google, a market benchmark against competitors, push
      notifications - and this website.
closingTitle: Fair by design
---

IceFlow is deliberately designed **not to be hard pay-to-win**. Players and competitive
currencies cannot be bought directly, and premium items can also be earned in the game.

That is possible because there is no big team to pay. A game made by one person does not have
to squeeze its players - it only needs to be good enough that people enjoy coming back to it.
