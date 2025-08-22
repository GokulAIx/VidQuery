from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled

def Trans(video_id):
    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)
        final_transcripts = " ".join(chunk.text for chunk in transcript)
        return final_transcripts

    except TranscriptsDisabled:
        
        return None

