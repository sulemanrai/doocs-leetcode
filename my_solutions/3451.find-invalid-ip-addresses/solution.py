def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    def is_valid_ip(ip: str) -> bool:
        # TODO: implement
        pass
    logs["is_valid"] = logs["ip"].apply(is_valid_ip)
