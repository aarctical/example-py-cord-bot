# Example py-cord bot

A basic bot that will give you some pointers on how to start making a bot using py-cord!

## Authors

- [@aarctical](https://www.github.com/aarctical) ([Discord](https://discord.com/users/423187100264038400))

## Requirements

#### Ensure discord.py is **not** installed!
You can do this by running ```python -m pip uninstall discord.py discord -y``` in the console.

```http
  py-cord
```

| PIP Line | Type     | Information               |
| :-------- | :------- | :------------------------- |
| `python -m pip install py-cord` | `console` | **Required** |


## Usage/Examples

```python
... # Cog Class

@commands.slash_command(name="ping")
async def ping(self, ctx):
  await ctx.respond("pong!", delete_after=3, ephemeral=True)
```


## Support

Any issues with the bot's function should be reported to [@aarctical](https://www.github.com/aarctical)

[Support Server Discord](https://discord.gg/mTKZynb)


## License

[MIT](https://choosealicense.com/licenses/mit/)
