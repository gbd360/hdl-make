library gatelib;

entity gate8 is
  port (i : in bit;
        o : out bit);
end gate8;

architecture behav of gate8 is
begin
  inst: entity gatelib.gate
    port map (i, o);
end behav;
