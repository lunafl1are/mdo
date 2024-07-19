from abc import ABC, abstractmethod

class IAirfoil(ABC):

  def Cl(self) -> tuple:
    raise NotImplementedError

  def Cd(self) -> tuple:
    raise NotImplementedError

  def Cm(self) -> tuple:
    raise NotImplementedError

  @abstractmethod
  @property
  def Cl_max(self) -> float:
    raise NotImplementedError

  @abstractmethod
  @property
  def Cd_min(self) -> float:
    raise NotImplementedError


