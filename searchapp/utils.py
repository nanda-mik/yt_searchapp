
def parse_youtube_videos(results):
    """
    Utility function to handle parsing logic as required for store.
    """
    parsed_results = [obj.get('snippet', {}) for obj in results]
    return parsed_results
