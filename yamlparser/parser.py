#========================================= yaml_parser.py =========================================#
#                                                                                                  #
#   Property of Daniel Sturdivant. Unauthorized copying of this file via any medium is would be    #
#   super sad and unfortunate for me. Proprietary and confidential.                                #
#                                                                                                  #
# ------------------------------------------------------------------------------------------------ #
#                                                                                                  #
#   @file                                                                                          #
#   @brief    This class is a wrapper for the python YAML library, it adds functionality to read   #
#             '*.yml' or  *.yaml' files into python dictionaries!                                  #
#   @author   Daniel Sturdivant <sturdivant20@gmail.com> <dfs0012@auburn.edu>                      #
#   @date     November 2023                                                                        #
#                                                                                                  #
#==================================================================================================#

import yaml, os

class YamlParser:

  # === init ===
  # YamlParser constructor
  def __init__(self, *args):
    # get absolute file path and save filename
    if len(args) == 2:
      self.path_ = os.path.join(os.getcwd(), args[0])
      self.filename_ = os.path.join(self.path_, args[1])
    else:
      full_path = os.path.realpath(args[0])
      self.path_ = os.path.dirname(full_path)
      self.filename_ = full_path

  # === ChangeFile ===
  # change the file being used by YamlParser
  def ChangeFile(self, *args):
    # get absolute file path and save filename
    if len(args) == 2:
      self.path_ = os.path.join(os.getcwd(), args[0])
      self.filename_ = os.path.join(self.path_, args[1])
    else:
      full_path = os.path.realpath(full_path)
      self.path_ = os.path.dirname(full_path)
      self.filename_ = full_path

  # === DumpYaml ===
  # Write a dictionary into a yaml file
  def DumpYaml(self, d):
    with open(self.filename_, 'w') as f:
      yaml.safe_dump(d, f, default_flow_style=None)
    return

  # === LoadYaml ===
  # Read a yaml file into a dictionary and checks for 'default' files
  def LoadYaml(self):
    with open(self.filename_, 'r') as f:
      self.d_ = yaml.safe_load(f)
    return self.d_

  # === Yaml2Dict ===
  # Read yaml file contents into python dictionary
  def Yaml2Dict(self):
    if not hasattr(self, "d_"):
      self.LoadYaml()
    if "default" in self.d_:
      self.d_ = self.__LoadNew(self.filename_)
    return self.d_
  
  # === GetVariable ===
  # Grab a specific variable from the yaml file
  def GetVariable(self, *args):
    d = self.d_
    for arg in args:
      d = d[arg]
    return d
  
  # === LoadNew ===
  # load default file recursively
  def __LoadNew(self, filename):
    with open(filename) as f:
      new = yaml.safe_load(f)

    # if 'default' then return
    if new['default'] is None:
      return new
    
    # recursively update
    base_filename = os.path.join(self.path_, new["default"])
    base = self.__LoadNew(base_filename)
    return self.__UpdateOverwrite(base, new)

  # === UpdateOverwrite ===
  # overwrite 'default' yaml file with parameters from higher level yaml file
  def __UpdateOverwrite(self, base, new):
    for k,v in new.items():
      if isinstance(v, dict) and isinstance(base.get(k, None), dict):
        base[k] = self.__UpdateOverwrite(base[k], v)
      else:
        base[k] = v
    return base


