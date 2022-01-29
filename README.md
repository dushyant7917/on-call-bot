# on-call-bot


### Note for client (event processing) service
The event processing service should expect json as input in the below format
```
{
    "token": "UYzgwmuqFfomHvBOWbfwxNJ8",
    "team_id": "T0311RCGMFB",
    "api_app_id": "A030SMMC119",
    "event": {
        "client_msg_id": "fd39dab6-6604-4d6d-b538-d588612e33cb",
        "type": "message",
        "text": "dfsdf",
        "user": "U030P6ULF6W",
        "ts": "1643453083.391979",
        "team": "T0311RCGMFB",
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "nk05",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [{"type": "text", "text": "dfsdf"}],
                    }
                ],
            }
        ],
        "channel": "C0308JK0G6B",
        "event_ts": "1643453083.391979",
        "channel_type": "channel",
    },
    "type": "event_callback",
    "event_id": "Ev030PPV1ALV",
    "event_time": 1643453083,
    "authorizations": [
        {
            "enterprise_id": None,
            "team_id": "T0311RCGMFB",
            "user_id": "U030SLXSWRY",
            "is_bot": True,
            "is_enterprise_install": False,
        }
    ],
    "is_ext_shared_channel": False,
    "event_context": "4-eyJldCI6Im1lc3NhZ2UiLCJ0aWQiOiJUMDMxMVJDR01GQiIsImFpZCI6IkEwMzBTTU1DMTE5IiwiY2lkIjoiQzAzMDhKSzBHNkIifQ",
}

```
