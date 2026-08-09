entity gate7_top is
  port (i : in bit;
        o1 : out bit;
        o2 : out bit);
end gate7_top;

architecture behav of gate7_top is
begin
  inst_one: entity work.gate7(one)
    port map (i, o1);
  inst_two: entity work.gate7(two)
    port map (i, o2);
end behav;
