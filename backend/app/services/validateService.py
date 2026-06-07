from app.database.connection import records
from datetime import datetime
from groq import Groq
import json
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq( api_key = os.getenv( "GROQ_API_KEY" ) )

PROMPT = """You are an expert hallucination detector.

Your task is to evaluate an LLM-generated answer.

Perform exactly three tests:

1. Verifiable Evidence Test (VET)
   - Check whether citations, studies, URLs, references, reports, organizations, or sources mentioned in the answer are real and verifiable.
   - Flag fabricated, unverifiable, or unsupported references.

2. Claim Support Test (CST)
   - Identify factual claims, statistics, percentages, rankings, measurements, dates, or causal claims that lack supporting evidence.
   - Flag unsupported assertions.

3. Consistency Test (CT)
   - Detect internal contradictions or mutually incompatible statements.

For each test provide:
- score (0 to 1)
- confidence (0 to 100)
- evidence from the text

Then compute:

Risk Score =
0.45 * VET +
0.35 * CST +
0.20 * CT

Provide the exact reason in english words on why you arrived to the concclusion.
Do not add any details about risk score, confidence in the reason
There should be exactly one reason per input. 
This reason is the one that affects the result the most.
State which test affected the result the most.
Do not add extra wordings to it.

Final confidence is based upon the confidence values of each test.

Return JSON:
{
  "result": "GOOD" | "BAD",
  "confidence": float,
  "reason": [...]
}

result depends on the Risk Score

result thresholds:
0.00-0.50 -> GOOD
0.50-1.00 -> BAD."""

async def check ( data : dict ):
    
    response = await getResponse( data[ 'text' ] )
   #  print( "response: \n", response )
    if data.get( 'expected', "not_exists" ) != "not_exists":
        print( "adding to records" )
        timestamp = datetime.now()
        records.insert_one( { 
            "timestamp" : timestamp, 
            "text" : data[ "text" ], 
            "result" : response[ "result" ], 
            "reason" : response[ "reason" ], 
            "confidence" : response[ "confidence" ],
            "expected" : data[ "expected" ]
        } )
    return response


async def getResponse( text: str ):
    
    user_input = "\nEvaluate the following answer:\n\n" + text

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": PROMPT
            },
            {
                "role": "user",
                "content": user_input
            }
        ],
        temperature=0,
        response_format={"type": "json_object"}
    )

    return json.loads(
        response.choices[0].message.content
    )