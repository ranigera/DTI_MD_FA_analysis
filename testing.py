# %%
import platform
print(platform.system())
print(platform.release())
print(platform.version())

# %%
running_on = 'server' if 'Linux' in platform.system() else 'my_mac'
running_on

# %%
