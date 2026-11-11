---
title: The story of Ice Flow
description: How Ice Flow, an online ice hockey manager for mobile, was designed and built by one developer working with AI between April and November 2026.
lead: >-
  Ice Flow: Hockey Manager is an online ice hockey management game for mobile, developed by a single person.
  Except for part of the graphics, which was finished in Photoshop, roughly 99 % of the work - game
  design, server, mobile app, tooling and texts - was produced in conversation with AI, largely
  during walks with a baby stroller. The project is meant as a practical test of how far one
  person with the relevant expertise can take a complex product with today's AI.
stats:
  - value: '1'
    label: developer
  - value: '7'
    label: months of development, April - November 2026
  - value: '4'
    label: codebases - engine prototype, server, mobile app, animation editor
  - value: '1,700+'
    label: commits
  - value: '~256,000'
    label: lines of code
  - value: '10'
    label: languages localised from the start
storyTitle: How it was built
areasTitle: What the game contains
areasIntro: >-
  An overview of the main systems as of November 2026. Numbers are the current game settings and
  may change during balancing.
areas:
  - title: Live coaching
    text: >-
      Matches are simulated on the server and streamed to the app as they are played. The coach can
      intervene at any point, not only between periods.
    facts:
      - Four full lines, a starting and backup goalie, two power-play and two penalty-kill units
      - 6 offensive and 6 defensive tactics plus 5 risk levels, set per line
      - Energy drains during a shift and recovers on the bench; accumulated fatigue limits starting energy
      - Line changes, line mixing, goalie pull and special teams can be changed during play
      - Delayed penalties, 3-on-3 overtime and empty net are modelled as real game states
      - Match state is pushed from the server every second over SSE
  - title: Match presentation
    text: >-
      Goals and selected chances are shown as animated highlights derived from the actual match
      events. They are not a physical replay, but they keep the game context.
    facts:
      - All goals plus additional chances, spread evenly through the match
      - Animation variant chosen by manpower situation (5v5, 6v5 empty net, 5v3 power play and others)
      - Variants for goals with zero, one or two assists
      - Clips are authored in a dedicated animation editor built for the project
  - title: Players as long-term systems
    text: >-
      A player's value is not a single number. Ratings, experience, form and traits develop at
      different rates over a career, so two players with the same ratings can differ substantially.
    facts:
      - Prospects are scouted at 17; their ratings and traits (TRT) are shown as ranges that scouting reports narrow
      - Development from 18 through team and individual training, with lower gains on the farm team
      - Experience stabilises performance and energy management; form reflects roughly the last 10-20 games
      - Mentality grows with exposure to important matches; discipline affects penalties and fights
      - Injury resistance declines with age and after serious injuries
      - Veterans play more steadily but lose speed and stamina until they retire
  - title: Club management
    text: >-
      Training, farm team, contracts, transfer market, facilities and finances are connected, so a
      decision in one area has consequences in the others.
    facts:
      - The farm team plays its own competition alongside the first team
      - Contracts up to 5 seasons; salary depends on ratings, age and expected development, plus a signing bonus
      - Transfer market with asking prices of 80-110 %, an 8-minute auction after the first bid and a 90-second soft close
      - Two currencies - Flow for running the club, Gold Pucks for the market, scouting and juniors
      - One cash and one gold-puck sponsor a season, each chosen from three kinds of offer
      - Arena and staff facilities (coaching, medical, scouting, front office, player development) with condition and repairs
  - title: Season and competitions
    text: >-
      A season lasts 21 real days. The calendar is short, but every block of the day carries
      decisions.
    facts:
      - 63 blocks per season - 21 days, three parts of each day
      - 12-team leagues, everyone plays everyone four times - 44 league games
      - Playoffs - quarter-finals to two wins, semi-final and final as single games
      - Elite league - 24 teams, 6 Swiss-system rounds, top 16 to the playoff, on the same calendar as the league
      - Rapid league - 4 teams, round robin, played instantly, with no fatigue, injuries or effect on league statistics
      - Match importance comes from the real table situation and can differ for each team
  - title: Simulation calibration
    text: >-
      The match engine is calibrated against long-term real-world hockey averages and checked over
      long simulated runs.
    facts:
      - Targets per team and game - about 29 shots on goal, 3.1 goals, 89.7 % save percentage, 2.8 power plays
      - Separate checks for the gap in team strength, goalie impact, risk, crowd, form and fatigue
      - 15-season runs check that development, mentality and discipline do not drift
      - The same match is replayed under the same conditions from stored snapshots
timelineTitle: Timeline
milestones:
  - date: April 2026
    phase: idea
    phaseLabel: Concept
    title: Concept in conversation
    text: >-
      Design work starts without code: what a mobile hockey manager should offer, how live coaching
      and long-term player development should work, and how the economy should stay balanced.
  - date: 27 April 2026
    phase: engine
    phaseLabel: Engine prototype
    title: First match engine prototype
    text: >-
      A Python prototype simulates matches period by period - shifts, line changes, zone play and
      goals. It serves as the environment for tuning the game rules.
  - date: May 2026
    phase: engine
    phaseLabel: Engine prototype
    title: Simulation depth
    text: >-
      Advanced statistics, goalie model, score-state effects and match form. The engine is
      refactored and calibrated against real-world numbers.
  - date: Early June 2026
    phase: engine
    phaseLabel: Engine prototype
    title: Management and economy model
    text: >-
      The prototype gains a management module - salaries, facility maintenance, match income,
      fatigue and injuries - and an economy tested over many seasons.
  - date: 10 June 2026
    phase: server
    phaseLabel: Server
    title: Game server
    text: >-
      Development of the production server starts in Kotlin and Quarkus with PostgreSQL - club
      generator, training progression and, within four days, a fully simulated league season.
  - date: Late June 2026
    phase: mobile
    phaseLabel: Mobile app
    title: Mobile app and transfer market
    text: >-
      The Flutter app starts on 24 June and is localised two days later. The server adds junior
      scouting, the transfer market, Redis, facilities, and lines and tactics.
  - date: July 2026
    phase: server
    phaseLabel: Server
    title: Core systems
    text: >-
      The most intensive month, with around 600 commits across server and app - playoffs, a
      real-time market over SSE, sponsors, nationalities, club logos and kit colours, the Elite league,
      the arena, bot clubs, and the prototype's match form ported into the server engine.
  - date: August 2026
    phase: animation
    phaseLabel: Animation
    title: Live match and animation editor
    text: >-
      A live-match mode with in-game changes to lineups, tactics and goalies. On 24 August a
      separate animation editor is created; its goal animations are integrated into the app the
      same day.
  - date: September 2026
    phase: server
    phaseLabel: Server
    title: Online stability
    text: >-
      A single authoritative server clock, locking clubs during their matches, load testing with a
      bot runner, deadlock fixes, query optimisation, and the farm competition in the app.
  - date: October 2026
    phase: engine
    phaseLabel: Engine and economy
    title: Calibration, onboarding and monetisation
    text: >-
      Engine recalibration against NHL data and a documented tactics model. Registration and a
      guided tutorial, then the Stars currency, daily and season tasks, the Rapid league, the store
      and 25 lifetime achievements.
  - date: Early November 2026
    phase: launch
    phaseLabel: Launch preparation
    title: Preparing for launch
    text: >-
      67 new live-match animations, mentality, discipline and form, match importance from the
      table, Sign in with Google, a competitive market benchmark, push notifications and this
      website.
  - date: After launch
    phase: launch
    phaseLabel: Plans
    title: What comes next
    text: >-
      Planned, with no dates yet: contract negotiation with players and free agents (offer,
      counter-offer, accepted, rejected), features unlocked gradually as seasons are played, chemistry
      of forward lines and defense pairs, the effect of a player's natural position and stick side,
      penalty shots during a game, shorter Rapid league formats, better match animations and graphics,
      and servers for Europe, Asia and the Americas.
notes:
  - title: Business model
    paragraphs:
      - >-
        Players, Flow and Gold Pucks cannot be bought for money. The premium currency, Stars, is
        earned in the game - through daily tasks (10 per day, up to 210 per season), season tasks (130 per
        season), lifetime achievements (25 tracks with 5 levels each) and Rapid league entries
        (1-5 Stars each, one ad per entry, up to 10 per day).
      - >-
        Stars buy a new name or club colours; a logo and two passes valid for 21 days can be bought
        with Stars or with real money. The Ads Pass removes ads without changing any daily limits. The
        Sponsor Pass increases sponsor income in Flow and Gold Pucks by 20 %, which is a real
        economic advantage; renewable Star income alone is not enough to keep it active every
        season. Ice Flow is therefore not pay-to-win in the sense of buying players or strength, but
        paying does give a moderate long-term economic benefit.
      - >-
        Because the game is developed by one person, its running costs are low, and it does not
        need aggressive monetisation to be sustainable.
  - title: Current status
    paragraphs:
      - >-
        The technical foundation is ready for a closed or soft launch - Google sign-in, load testing
        with 288 bot clubs, a server-authoritative live match and deterministic match replays. What
        is still missing is evidence from real operation - reconnects, crash reports, retention and
        how the economy behaves with real players. The next phase is therefore a soft launch,
        telemetry and balancing rather than new features.
---

The idea for Ice Flow started in April 2026, before any code was written. The first weeks were
spent in conversation with AI, defining what the game should be: a mobile hockey manager where
decisions continue during the match, players develop over whole careers, and the online world
keeps running between sessions. Most of these conversations happened on walks with a baby
stroller - time that would otherwise not have been used for development.

The roles were split clearly from the start. The author acted as product owner and architect,
deciding on game design, priorities and trade-offs, and reviewing results. AI wrote the
implementation, tests, calibration experiments and documentation. A typical iteration was a
written specification, an implementation, an automated test run and an evaluation of the results
against the intended behaviour.

### From prototype to online game

The first working code, at the end of April, was a match engine prototype in Python. It served as
a laboratory: shifts, line changes, zone play, goalies, form and economy were modelled and
calibrated there before anything went into the real game. In June the production server was
started in Kotlin with Quarkus, PostgreSQL and Redis, and two weeks later the mobile app in
Flutter. Proven models from the prototype were then ported into the server engine.

When the live match needed visual highlights, a separate animation editor was written in Python
in August. The app uses its clips directly and picks a variant to match each event - the manpower
situation and the number of assists.

### Quality and verification

With one developer there is no QA team, so verification is built into the project itself. The
server has around 310 automated tests, the match engine is checked by calibration runs over
thousands of matches and by multi-season simulations, and bot clubs fill the leagues and generate
load. The help texts in the app are also checked against what the server actually does - the
audit in October 2026 found and corrected 14 mismatches across all ten languages. The goal is that
every change can be verified objectively, not only by playing.
