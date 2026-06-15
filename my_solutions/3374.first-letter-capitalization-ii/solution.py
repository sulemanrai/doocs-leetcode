def capitalize_content(user_content: pd.DataFrame) -> pd.DataFrame:
    def convert_text(text: str) -> str:
        # TODO: implement
        pass
    user_content["converted_text"] = user_content["content_text"].apply(convert_text)
