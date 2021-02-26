# nicks-birthday-2021

A tech-based birthday puzzle

# Overview

The challenge will be in three stages, each corresponding to a conversation
with a different chat bot:

- Discord
- Email
- Physical mail

# Overall Flow

1. Recieve email from email bot.
2. Email bot gives easy first puzzle which leads to discord bot.
3. Discord bot must be "defeated" before you can speak to the email bot again
4. Email bot has a secret master: _snail mail bot_

# Challenges

## Delivery & Initial Starting Point

### WAV

**Challenge**

WAV file will be sent to nick which plays the avenger's theme song. At the
end, the file will break down into jarbled white noise.

**Solution**

The garbled sound will actually be the link to the discord server concatenated
together over and over again.

## Discord Bot

### Server Config from WAV Metadata

**Challenge**

Correctly configure the server

**Solutaion**

Metadata from the WAV file specifies how the server should be set up.

| Key         | Value                    |
| ----------- | ------------------------ |
| members     | 4 minimum                |
| guild roles | 1 big boss, 3 small bois |

### "Have a Conversation!"

**Challenge**

Bot gives an ambiguous prompt. For example, "tell me what I want to know
about representative democracy."

**Solution**

There will be a target phrase or word. Once that word or phrase is sent
in any message, the puzzle will be unlocked. To make the puzzle _possible_,
after certain thresholds of overall messages sent are reached, clues
will be given.

### Generic Discord Bot Puzzles

**Challenge**

Generic chat puzzles such as from
[Puzzle Bot](https://github.com/franktzheng/puzzle-bot)

**Solution**

Solve puzzles.

### Chess Puzzle

**Challenge**

The discord bot initiates a chess puzzle

**Solution**

Solve the chess puzzle

## Email Bot

### Code Execution

**Challenge**

Why is the emailer send back tracebacks?? Is this thing executing code?

**Solution**

The emails recieved will be directly executed inside an arbitrary code
execution engine. The execution environment will include things in
the local scope which Nick must inspect, discover, and interact with. `stdout`
and `stderr` will be his inbox.

There will actually be four puzzles here of increasing complexity. The puzzle
will be solved and advanced when Nick is able to get the right information
into the program input, but he may have to uncover hidden secrets from
data in the scope of the program before that will be possible.

_Other Notes_

- Use emojis

## Snail Mail Bot: **The Pony Express**

Mail bot can be thought of as the "final boss." For these puzzles, Nick
will have to wait days to find out if his clue was correct. If the messages
are long and/or encrypted, he will have to type them accurately before
he can work with them programmatically.

[This API](https://developers.clicksend.com/docs/rest/v3/#ClickSend-v3-API-Post-Letter)
is what we will use.
