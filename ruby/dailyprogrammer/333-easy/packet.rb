
class Packet
    attr_accessor :message_id
    attr_accessor :packet_id
    attr_accessor :packet_count
    attr_accessor :content
    
    def initialize(mid, pid, pc, text)
        @message_id = mid
        @packet_id = pid
        @packet_count = pc
        @content = text
    end
    
    def print
        printf("%d  %d %d %s\n", @message_id, @packet_id, @packet_count, @content)
    end
end

# Inefficient, iterates through all packets for each print time complex. O(n^2) for n packets
def completeMessage(packets, message_id, packet_count)
    # Python: for i in range(1,packet_count)
    (0..packet_count).each do |i|
        for p in packets
            if p.message_id == message_id && p.packet_id.to_i == i
                p.print
                # Deleting while iterating seems safe in ruby
                packets.delete(p)
            end
        end
    end
end

# Python: if __name__ == __main__
if __FILE__ == $0
    # Python: packet_count = {}
    packet_count = Hash.new
    fd = open(ARGV[0], 'r+')
    packets = []
    begin
        for line in fd
            str = line.split(' ')
            # Create packet for each line
            packets += [Packet.new(str[0], str[1], str[2], str[3..str.size].join(' '))]
            # Update count for message id
            if packet_count[str[0]]
                packet_count[str[0]] += 1
            else
                packet_count[str[0]] = 1
            end
            # If count has reached packet_count, we have all packets and can print message
            if packet_count[str[0]].to_i == str[2].to_i
                completeMessage(packets, str[0], str[2].to_i)
            end
        end
    ensure #Python: finally
        fd.close
    end
end
