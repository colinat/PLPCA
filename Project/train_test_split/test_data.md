## intent:greet
- hi
- good evening

## intent:goodbye
- goodnight
- good bye
- bye

## intent:thanks
- Thanks for that
- Thank u

## intent:ask_what_can_u_do
- what can u do
- help me

## intent:inform
- [sales](aspect_type)
- [products_services](aspect_type)

## intent:query_sentiment
- Will there be any new upcoming new [products](aspect_type) or services launches that we can look forward to?
- Is CEO [optimistic](emot_polarity) about the current pandemic [risks](aspect_type:op_risks) subsiding within the next year
- Can we expect to see greater [competition](aspect_type) and operating risks to the company in the coming year?
- Are there risks to current [profit margin](aspect_type:earnings) from any upcoming expenses?
- Is the global shutdown or protests in the city likely to be [detrimental](sent_polarity) to the operations of the company
- Have interest rate trends benefited/acted against the company?
- Is management [optimistic](emot_polarity)?
- What does management [feel](emot_polarity) about the [competitive landscape](aspect_type:competition) in the near term for the company?
- Is company expected to be active on the merger and acquistion front this year?
- Can we expect to see accelerating return from the investments?
- Would the CEO expect the [negative](sent_polarity) trend to reverse?

## intent:query_sentence
- What caused margin [to decline](sent_polarity:negative)?
- What is holding back the [sales](aspect_type) growth this quarter?
- Should we expect to see a net impact in margin?
- Any particular costs that might impact [earnings](aspect_type) going forward investors should be concerned about?

## intent:out_of_scope
- can you learn from our conversation?
- and make chicken noises into the phone
- I want a new laptop
- cannot see
- common, just try
- I'm a shitmuncher
- Can you call me back ?
- can you cook dinner
- connect to alexa
- I am an opioid addic
- Order me a pizza
- What day is it today?
- again?
- What is your hobbies?
- can you help me with your docs
- Pizza bot
- can you help me with your docs?
- What's 1 + 1?
- Can you please send me an uber
- I ned a GP in 94301
- I am hungry
- Find nearest pizzahut
- can you give me a cup of coffee
- What is todays date

## intent:bot_challenge
- am I talking to a bot?

## synonym:acquisitions
- aquisition
- acquisituoin
- buyout
- M&A
- mergers

## synonym:competition
- competitors
- competitive landscape
- challengers

## synonym:confident
- optimistic

## synonym:debt
- gearing
- leverage
- geared
- liquidity
- financing
- loan
- loans

## synonym:earnings
- margins
- profit margin
- stock price
- performance
- bottom line
- net profit
- bottomline
- eps
- EPS
- result
- net margin
- net margins

## synonym:negative
- to decline
- rising costs

## synonym:op_costs
- operating costs
- costs
- expenses
- gross margin
- gross margins
- cost
- overheads
- opex
- operational cost
- operation cost
- operating cost
- operational expense
- operation expense

## synonym:op_risks
- risks
- challenges
- business risks
- operational risk
- operation risk
- operating risk
- ops risks

## synonym:organic_expansion
- expansion
- expansion plans
- growth strategy

## synonym:products_services
- products
- business
- business division
- biz

## synonym:sales
- revenue
- sales
- net revenue
- topline
