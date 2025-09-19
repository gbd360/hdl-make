module json_test (
    input  logic i_clk,
    input  logic i_rst_n,
    output logic led_o
);

logic [31:0] cnt;
always_ff @(posedge i_clk) begin
    if (!i_rst_n) cnt <= '0;
    else cnt <= cnt + 1'b1;
end

assign led_o = cnt[$high(cnt)];

endmodule : json_test
