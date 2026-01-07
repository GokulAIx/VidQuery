from fastapi import FastAPI, HTTPException
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
import traceback

app = FastAPI()

def Trans(video_id: str):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        final_transcripts = " ".join(chunk['text'] for chunk in transcript)
        return final_transcripts
    except TranscriptsDisabled:
        return None
    except NoTranscriptFound:
        return None
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        traceback.print_exc()
        return None

@app.get("/transcript/{video_id}")
async def get_transcript(video_id: str):
    try:
        transcript_text = Trans(video_id)
        if transcript_text is None or len(transcript_text.strip()) == 0:
            raise HTTPException(
                status_code=404,
                detail="No transcripts available for this video."
            )
        # Return plain text for consistency with app.py expectations
        return transcript_text
    except HTTPException:
        raise
    except Exception as e:
        print(f"Unexpected error: {e}")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail=f"Server error: {str(e)}"
        )
