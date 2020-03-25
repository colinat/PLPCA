## intent:greet
- hi
- hi again

## intent:goodbye
- bye
- see you later
- good bye

## intent:thanks
- Thanks
- thanks

## intent:ask_what_can_u_do
- what do u do?
- what can u do

## intent:inform
- [competition](aspect_type)
- [sales](aspect_type)

## intent:query_sentiment
- How are cashflows of the company and can we expect more paring down of [debt](aspect_type) going forward?
- Is the recent virus outbreak expected to pose huge [challenges](aspect_type:op_risks) for the company
- Is there expectation for growth to moderate?
- What is the general [tone](emot_polarity) of management?
- How have our [acquisitions](aspect_type) performed?
- Can we expect to see accelerating return from the investments?
- Is management expected to take on more [financing](aspect_type:debt) to grow the business?
- Is the supply chain disruption in China expected to pose any [challenges](aspect_type:op_risks) for company?
- How should we see any impacts on [revenue](aspect_type:sales)?
- Are we seeing inflationary [costs](aspect_type:op_costs) in the business and how it may be impacting comps?
- Have interest rate trends benefited/acted against the company?

## intent:query_sentence
- What has been the biggest [unexpected](sent_polarity) [cost](aspect_type:op_costs) that has impacted the company in the previous quarter?
- What caused margin [to decline](sent_polarity:negative)?
- Any changes in the [sales](aspect_type) trends?
- What are factors influencing [gross margin](aspect_type:op_costs)?

## intent:out_of_scope
- can you help me with your docs
- The weather is good
- Now?
- What makes you better than a human?
- I am hungry
- 4 + 2 = ?
- Is this Goal-Oriented Chatbot?
- aRE YOU SINGLE
- But you're an english site :(
- Can you give me your datacenter's password
- How long does it take to set up a Rasa bot?
- can you understand ?
- colder
- alexa, order 5 tons of natrium chloride
- Is today saturday?
- Order me a pizza
- Can you please send me an uber
- are you human ?
- can we keep chatting?
- Today
- I'm a shitmuncher
- I want french cuisine
- Who’s the US President?
- can you help me with your docs?

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
